import ast
import base64
import hashlib
import hmac
import json
import select
import subprocess
import sys
import time
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, '/root/Hotaru')
from relay.sandbox import WORKER_SOURCE, _TOOLKIT_SOURCE, _CONTEXT_SOURCE, _DENYLIST_SOURCE, _TRANSLATION_SOURCE, SECCOMP_POLICY
from hotaru.modules import HmodLoader
from hotaru.screens import ScreenEngine, ScreenError

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'vector.hmod'
SOURCE = PATH.read_text()
MANIFEST = ast.literal_eval(ast.parse(SOURCE).body[0].value)
MODULE = "HOTARU = {'id': 'example', 'version': '1', 'commands': [], 'capabilities': []}\n"
JWT = 'eyJhbGciOiJIUzI1NiJ9.' + base64.urlsafe_b64encode(json.dumps({'sub': '123', 'exp': time.time() + 3600}).encode()).decode().rstrip('=') + '.signature'


def main():
    loaded = HmodLoader().load(PATH)
    assert list(loaded.manifest.commands) == ['vector', 'vecupdate', 'vecdl', 'vecme']
    tree = ast.parse(SOURCE)
    assert not any(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
    assert not any(isinstance(n, ast.arg) and n.annotation is not None for n in ast.walk(tree))
    assert not any(x in SOURCE for x in ('self.client', 'self.inline', 'self.strings', '_Message', '_Strings', '_Client', '_context()', '_pending_inputs'))
    state, screens, responses, calls, files = {}, [], [], [], []
    scenario = {'source': MODULE, 'confirm': False, 'audit429': False}
    comments = [{'id': i, 'author_name': 'Alice', 'body': 'Comment ' + str(i)} for i in range(6)]
    rid = 0
    process = subprocess.Popen([sys.executable, '-s', '-S', '-c', WORKER_SOURCE], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def send(value):
        process.stdin.write(json.dumps(value) + '\n')
        process.stdin.flush()

    def read():
        assert select.select([process.stdout], [], [], 30)[0], 'Worker response timeout'
        line = process.stdout.readline()
        assert line, process.stderr.read()
        return json.loads(line)

    def service(message):
        if 'log' in message or 'heartbeat' in message or '_hb' in message:
            return
        if 'cap' in message and message['cap'] == 'mt':
            message['op_call'] = message.pop('payload')
            message.pop('cap')
        if 'cap' in message:
            capability = message['cap']
            data = message.get('payload', {})
            calls.append((capability, data))
            if capability == 'state':
                op, key = data['op'], data.get('key')
                if op == 'get': value = state.get(key)
                elif op == 'set': state[key] = data['value']; value = None
                elif op == 'delete': state.pop(key, None); value = None
                else: value = list(state)
            elif capability == 'net':
                url = data['url']
                if url.startswith('udp:'):
                    send({'cid': message['cid'], 'ok': False, 'error': 'NTP disabled by deterministic test; exercise HTTPS fallback'})
                    return
                if data.get('method') == 'HEAD':
                    value = {'status': 200, 'headers': {'Date': __import__('email.utils', fromlist=['formatdate']).formatdate(time.time(), usegmt=True)}, 'body': ''}
                else:
                    assert 'platform=hotaru' in url, url
                    code = 200
                    if '/api/tg-bot/install-feedback' in url: body = {'ok': True}
                    elif '/api/tg-bot' in url: body = {'username': 'vector_bot'}
                    elif '/source' in url:
                        value = {'status': 200, 'headers': {}, 'body': base64.b64encode(scenario['source'].encode()).decode(), 'encoding': 'base64'}
                        send({'cid': message['cid'], 'ok': True, 'result': value}); return
                    elif '/security-check' in url:
                        if scenario['audit429']: code = 429; body = {}
                        else: body = {'quota': {'remaining': 3, 'limit': 5}, 'check': {'verdict': 'safe', 'summary': 'No findings', 'details': {'static': {'findings': {}}}}} if data.get('method') == 'POST' else {'quota': {'remaining': 3, 'limit': 5}}
                    elif '/comments' in url:
                        if data.get('method') == 'POST': comments.append({'id': 99, 'author_name': 'Tester', 'body': data['data']['body']})
                        body = {'ok': True, 'comments': comments}
                    elif '/api/rate/' in url: body = {'ok': True, 'likes': 9, 'dislikes': 2, 'rating': {'state': 'added'}}
                    elif '/api/collections/' in url: body = {'ok': True, 'collection': {'name': 'Examples', 'modules': [{'module': {'name': 'Example', 'source_owner': 'owner', 'platform': 'hotaru'}}]}}
                    elif '/api/users/me/modules' in url: body = {'ok': True}
                    elif '/api/modules/by-id' in url: body = {'ok': True, 'module': {'name': 'Example', 'source_owner': 'owner'}}
                    else: body = {'results': [{'name': 'Example' + str(i), 'source_owner': 'owner', 'description': 'Useful module', 'likes': 1, 'commands': [{'name': 'hello', 'description': 'Hello'}], 'tags': ['tools'], 'dependencies': ['stdlib']} for i in range(7)]}
                    value = {'status': code, 'body': json.dumps(body), 'headers': {}}
            elif capability == 'modules':
                if data['op'] == 'info': value = {'digest': hashlib.sha256(scenario['source'].encode()).hexdigest()}
                elif data['op'] == 'list': value = [{'module_id': 'example', 'active': True, 'digest': 'abc'}]
                else: value = {'action': 'confirm' if scenario['confirm'] else 'loaded', 'capabilities': ['net']}
            elif capability == 'assets':
                value = {'id': 1, 'parts': 1, 'name': 'example.hmod', 'md5': ''}
                files.append(data)
            elif capability == 'fetch': value = {'id': 321, 'username': 'vector_bot', 'access_hash': 12345, '_': 'user'}
            else: raise AssertionError((capability, data))
            send({'cid': message['cid'], 'ok': True, 'result': value})
        elif 'op_call' in message or 'mt' in message:
            data = message.get('op_call') or message.get('mt')
            calls.append(('rpc', data))
            method = data['method']
            if method == 'users.getUsers': value = [{'id': 123, 'first_name': 'Tester'}]
            elif method == 'messages.getHistory':
                value = {'messages': [{'id': 103, 'from_id': 321, 'message': JWT}]} if scenario.get('sent_auth') else {'messages': []}
            elif method == 'messages.sendMessage':
                scenario['sent_auth'] = True
                value = {'updates': [{'message': {'id': 102}}]}
            elif method == 'account.getNotifySettings': value = {'mute_until': 0, 'silent': False}
            else: value = True
            send({'cid': message['cid'], 'ok': True, 'result': value})
        elif 'respond' in message:
            value = message['respond']
            responses.append(value)
            if 'prepare' in value:
                send({'cid': message['cid'], 'ok': True, 'result': {'message': value['prepare']['text'] or ''}})
                return
            if 'media_rpc' in value:
                calls.append(('rpc', value['media_rpc']))
                send({'cid': message['cid'], 'ok': True, 'result': {'id': 11}})
                return
            if 'screen' in value: screens.append(value['screen'])
            else: responses.append(value)
            send({'cid': message['cid'], 'ok': True, 'result': 10})
        elif 'cb_respond' in message:
            responses.append(message['cb_respond'])
            send({'cid': message['cid'], 'cb_respond_result': {'ok': True, 'result': None}})
        else: raise AssertionError(message)

    def request(command=None, raw='', target=None, payload=None, callback=None):
        nonlocal rid
        rid += 1
        base = {'chat_id': 123, 'message_id': 10, 'from_id': 123, 'out': True, 'language': 'en', 'prefix': '.', 'config': {k: v['default'] for k, v in MANIFEST['config_schema'].items()}, 'translations': {'vector': MANIFEST['lexicon']['en']['strings']}, 'raw_args': raw}
        base.update(payload or {})
        message = {'rid': rid, 'command': command or target, 'args': raw.split(), 'payload': base}
        if target: message['target'] = target
        if callback: message = {'rid': rid, 'cb': {'module_id': 'vector', 'action_id': 'vector_action', 'payload': callback, 'chat_id': 123, 'message_id': 10, 'from_id': 123}}
        send(message)
        while True:
            result = read()
            if result.get('rid') == rid and 'ok' in result and 'cid' not in result:
                assert result['ok'], result
                return result.get('result')
            service(result)

    try:
        cfg = {'module_id': 'vector', 'source': SOURCE, 'commands': MANIFEST['commands'], 'toolkit_source': _TOOLKIT_SOURCE, 'context_source': _CONTEXT_SOURCE, 'denylist_source': _DENYLIST_SOURCE, 'translation_source': _TRANSLATION_SOURCE, 'net_blocked': True, 'seccomp': SECCOMP_POLICY, 'namespaces': False, 'seccomp_required': False, 'protected': []}
        send(cfg)
        assert read()['ok']
        request('vector')
        assert responses
        request(target='task_token_keeper', payload={'source': 'task'})
        assert any(x[0] == 'rpc' and x[1]['method'] == 'users.getUsers' for x in calls), 'fresh auth exchange not exercised'
        assert state.get('auth_token') == JWT
        request('vector', 'tools')
        assert screens and '<h1>' in screens[-1]['text']
        key = screens[-1]['rows'][0][1]['payload']['session']
        def action(name, **kw): return request(callback={'session': key, 'action': name, **kw})
        action('nav', index=1)
        assert any('Example1' in x.get('text', '') for x in responses)
        action('list', page=1)
        action('toggle')
        action('like')
        assert state['menu:' + key]['group'][1]['likes'] == 9
        action('audit'); action('audit_run')
        assert state['audit:owner/Example1']['check']['verdict'] == 'safe'
        action('comments', page=1)
        assert screens[-1]['rows'][0][0]['k'] == 'input'
        assert screens[-1]['rows'][0][0]['f'] == 'comment_submit'
        action('install')
        assert 'example' in state['vector_inventory']
        scenario['source'] = 'from .. import loader\n'
        before = len([x for x in calls if x[0] == 'modules' and x[1]['op'] == 'load'])
        action('install')
        assert len([x for x in calls if x[0] == 'modules' and x[1]['op'] == 'load']) == before
        scenario['source'] = MODULE
        scenario['confirm'] = True
        action('install')
        assert state['vector_inventory']['example']['pending']
        assert files and files[-1]['filename'] == 'example.hmod', ('native .hmod export must exercise file path', responses[-6:], calls[-6:])
        assert any(x.get('action') == 'respond' and 'permission review required' in x.get('text', '') for x in responses[-4:]), responses[-4:]
        scenario['confirm'] = False
        request('vecdl', 'examples')
        collection_key = screens[-1]['rows'][0][0]['payload']['session']
        request(callback={'session': collection_key, 'action': 'collection'})
        request('vecme')
        assert 'startapp=hotaru' in screens[-1]['rows'][0][0]['url']
        request('vecupdate')
        assert screens[-1]['rows'][0][0]['payload']['action'] == 'update'
        request(target='task_sync_modules_keeper', payload={'source': 'task'})
        state['bot_id'] = 321
        secret = 'vektor_heroku_searchmodulesModbySepiol026-wqGithub'
        value = 'owner|Example:like:' + str(int(time.time()))
        signature = hmac.new(secret.encode(), value.encode(), hashlib.sha256).hexdigest()
        request(target='watcher_install', payload={'out': False, 'from_id': 321, 'text': '#v_payload_hotaru:' + value + ':' + signature})
        assert 'payload:' + signature in state
        assert any(x[0] == 'net' and '/install-feedback' in x[1]['url'] for x in calls)
        before = len(calls)
        request(target='watcher_install', payload={'out': False, 'from_id': 321, 'text': '#v_payload_hotaru:' + value + ':bad'})
        assert not any(x[0] == 'modules' and x[1]['op'] == 'load' for x in calls[before:])
        engine = ScreenEngine.__new__(ScreenEngine)
        active = SimpleNamespace(context=SimpleNamespace(namespace={'__sandbox__': True}))
        engine.runtime = SimpleNamespace(modules=SimpleNamespace(get=lambda _: active), sandbox=object())
        assert callable(engine._handler({'m': 'vector', 'f': 'comment_submit'}, SimpleNamespace(module='vector')))
        assert '86400' not in SOURCE
        print('PASS external native input resolves sandbox bridge; menus have no time-based expiration')
        print('PASS actual WORKER_SOURCE: manifest/architecture, empty/search/rich cards, navigation/list/toggle, rating, audit GET+POST, native inline input descriptor, safe install/reject/consent export, collection, Mini App, update digest prompt, inventory task, signed payload/feedback and invalid signature rejection. Host API responses are deterministic test doubles; no live Telegram/backend claims.')
    finally:
        process.terminate()
        process.communicate(timeout=10)


if __name__ == '__main__':
    main()
