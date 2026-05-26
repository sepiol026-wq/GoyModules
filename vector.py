# ====================================================================================================================
#   ██████╗  ██████╗ ██╗   ██╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
#  ██╔════╝ ██╔═══██╗╚██╗ ██╔╝████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
#  ██║  ███╗██║   ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ███████╗
#  ██║   ██║██║   ██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║
#  ╚██████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗███████║
#   ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
#
#   OFFICIAL USERNAMES: @goymodules | @samsepi0l_ovf
#   MODULE: vector
#
#   THIS MODULE IS LICENSED UNDER GNU AGPLv3, PROTECTED AGAINST UNAUTHORIZED COPYING/RESALE,
#   AND ITS ORIGINAL AUTHORSHIP BELONGS TO @samsepi0l_ovf.
#   ALL OFFICIAL UPDATES, RELEASE NOTES, AND PATCHES ARE PUBLISHED IN THE TELEGRAM CHANNEL @goymodules.
# ====================================================================================================================
# meta banner: https://raw.githubusercontent.com/sepiol026-wq/GoyModules/refs/heads/main/assets/vector.png
# meta developer: @GoyModules

__version__ = (2, 2, 8)

import asyncio
import base64
import hashlib
import hmac
import json
import logging
import os
import re
import time
import unicodedata
from contextlib import suppress
from typing import Any, Dict, List, Optional
from urllib.parse import quote, urljoin

import aiohttp
from herokutl.tl.functions.contacts import UnblockRequest
from herokutl.types import Message

from .. import loader, utils

log = logging.getLogger("VectorMonolith")
log.setLevel(logging.INFO)

API_ROOT = "https://vector-three-sooty.vercel.app"
JWT_REGEX = re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")
AUTH_SALT = "vektor_heroku_searchmodulesModbySepiol026-wqGithub"
OFFICIAL_CREATORS = {"@goymodules", "@samsepi0l_ovf"}
OFFICIAL_VECTOR_BOT_ID = int(os.getenv("VECTOR_OFFICIAL_BOT_ID", "0"))
LANG_PING_PAYLOAD = "#v_lang_ping"
LANG_PONG_PREFIX = "#v_lang:"
BAN_REASON_RE = re.compile(r"(?:Причина|Reason|理由|Grund|R3450n|Weason|Charge):\s*(.+)", re.IGNORECASE)
BAN_TERM_RE = re.compile(r"(?:Срок|Term|期間|Dauer|73rm|Tewm):\s*(.+)", re.IGNORECASE)

@loader.tds
class Vector(loader.Module):
    """Vector module registry browser for Heroku."""

    strings = {
        "lang": "en",
        "name": "Vector",
        "_cls_doc": "Vector module registry browser for Heroku.",
        "v_dev_lbl": "Author:",
        "v_dev_str": "Dev:",
        "v_dev_ofc": "official",
        "v_dev_unofc": "unofficial",
        "v_info": "Info:",
        "v_cmds": "Usage:",
        "v_reqs": "Libs:",
        "v_hid_cmd": "+ {rem} hidden cmds.",
        "v_hid_req": "+ {rem} hidden libs.",
        "v_res_hdr": "Found Items:",
        "v_err_empty": "Specify query: {p}vector <text>",
        "v_err_404": "No records for: {q}",
        "v_err_len": "Query length is limited to 120 chars.",
        "v_err_api": "Access denied by Vector Server.",
        "v_ban_notice": "⛔ <b>Vector access blocked.</b>\n<b>Reason:</b> <code>{reason}</code>\n<b>Term:</b> <code>{term}</code>",
        "v_fb_add": "Rated successfully!",
        "v_fb_rm": "Rating cleared!",
        "v_btn_copy": "Query",
        "v_btn_dl": "Install",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "Source",
        "v_dl_ok": "Module installed successfully!",
        "v_dl_err": "Installation failed!",
        "v_lim_cfg": "Search output limits.",
        "v_btn_sec": "🛡 Security Scan",
        "v_aud_hdr": "Code Audit: {name}",
        "v_aud_req": "Connecting to Security API...",
        "v_aud_proc": "Processing AST tree...",
        "v_btn_aud_run": "Start Scan",
        "v_aud_mem": "Loaded from session cache.",
        "v_aud_lvl": "Threat Level",
        "v_aud_stat": "Scanner Data",
        "v_aud_out": "Summary",
        "v_aud_sigs": "Triggers",
        "v_sig_crit": "Critical",
        "v_sig_warn": "Warnings",
        "v_sig_info": "Notices",
        "v_aud_none": "Not scanned yet. Takes 1 API slot.",
        "v_aud_no_txt": "No summary generated.",
        "v_aud_left": "Slots left: {remaining}/{limit}",
        "v_aud_zero": "Daily audit limit depleted.",
        "v_aud_err": "Scanner server is down.",
        "v_err_gui": "Interface rendering error.",
        "v_btn_exp": "🔽 Expand",
        "v_btn_col": "🔼 Collapse",
        "v_btn_talk": "💬 Discussion",
        "v_talk_hdr": "{emoji} <b>Thread: {name}</b>",
        "v_talk_desc": "Community reviews",
        "v_talk_num": "Posts: {count}",
        "v_talk_0": "Thread is empty. Be the first!",
        "v_talk_err": "Could not connect to thread.",
        "v_rep_ok": "Posted!",
        "v_rep_err": "Request failed.",
        "v_btn_bck": "⬅️ Back",
        "v_btn_site": "🌐 Web View",
        "v_btn_wrt": "✍️ Post Reply",
        "v_rep_ask": "Reply to post message.\n2-1800 chars.",
        "v_rep_snt": "Uploading...",
        "v_rep_min": "Text is too short.",
        "v_rep_max": "Limit exceeded.",
        "v_rep_cncl": "Cancelled.",
        "v_loading_ui": "Searching Vector database...",
        "v_more_replies": "...and {count} more replies on the site.",
        "v_more_comments": "...and more comments on the site.",
        "v_upd_req": "Updating Vector...",
        "v_upd_ok": "Vector updated successfully!",
        "v_upd_err": "Update failed!",
        "v_install_log_hdr": "Install log: {name}",
        "v_install_fail_forbidden": "Forbidden method: <code>{detail}</code>",
        "v_install_fail_requirements": "Pip deps failed: <code>{detail}</code>",
        "v_install_fail_dependency": "Missing dependency: <code>{detail}</code>",
        "v_install_fail_packages": "System pkgs failed: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "Tried to overwrite core <code>{detail}</code>",
        "v_install_fail_ffmpeg": "Requires ffmpeg (not installed)",
        "v_install_fail_inline": "Requires inline mode (unavailable)",
        "v_install_fail_heroku_min": "Needs Heroku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "Not found in configured repos",
        "v_install_fail_download": "Failed to download module",
        "v_install_fail_unknown": "Unknown error: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>You are on the latest version. Update anyway?</b>",
        "v_upd_force_btn": "🧭 Update",
        "v_upd_cancel": "🚫 Cancel",
    }

    strings_ru = {
        "lang": "ru",
        "_cls_doc": "Обозреватель реестра модулей Vector для Heroku.",
        "v_dev_lbl": "Автор:",
        "v_dev_str": "Разраб:",
        "v_dev_ofc": "офиц",
        "v_dev_unofc": "неофиц",
        "v_info": "Инфо:",
        "v_cmds": "Использование:",
        "v_reqs": "Библиотеки:",
        "v_hid_cmd": "+ скрыто команд: {rem}.",
        "v_hid_req": "+ скрыто либ: {rem}.",
        "v_res_hdr": "Найденные модули:",
        "v_err_empty": "Укажите запрос: {p}vector <текст>",
        "v_err_404": "Нет записей по запросу: {q}",
        "v_err_len": "Длина запроса ограничена 120 символами.",
        "v_err_api": "Отказ в доступе от сервера Vector.",
        "v_ban_notice": "⛔ <b>Доступ к Vector заблокирован.</b>\n<b>Причина:</b> <code>{reason}</code>\n<b>Срок:</b> <code>{term}</code>",
        "v_fb_add": "Оценка добавлена!",
        "v_fb_rm": "Оценка удалена!",
        "v_btn_copy": "Запрос",
        "v_btn_dl": "Установить",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "Исходник",
        "v_dl_ok": "Модуль успешно установлен!",
        "v_dl_err": "Ошибка установки!",
        "v_lim_cfg": "Лимиты вывода поиска.",
        "v_btn_sec": "🛡 Проверка кода",
        "v_aud_hdr": "Аудит кода: {name}",
        "v_aud_req": "Соединение с Security API...",
        "v_aud_proc": "Анализ AST дерева...",
        "v_btn_aud_run": "Запустить скан",
        "v_aud_mem": "Загружено из кэша сессии.",
        "v_aud_lvl": "Уровень угрозы",
        "v_aud_stat": "Данные сканера",
        "v_aud_out": "Итог",
        "v_aud_sigs": "Триггеры",
        "v_sig_crit": "Критично",
        "v_sig_warn": "Внимание",
        "v_sig_info": "Уведомления",
        "v_aud_none": "Еще не проверен. Расходует 1 слот API.",
        "v_aud_no_txt": "Описание не сгенерировано.",
        "v_aud_left": "Остаток слотов: {remaining}/{limit}",
        "v_aud_zero": "Суточный лимит проверок исчерпан.",
        "v_aud_err": "Сервер сканирования недоступен.",
        "v_err_gui": "Сбой рендеринга интерфейса.",
        "v_btn_exp": "🔽 Развернуть",
        "v_btn_col": "🔼 Свернуть",
        "v_btn_talk": "💬 Обсуждение",
        "v_talk_hdr": "{emoji} <b>Тред: {name}</b>",
        "v_talk_desc": "Отзывы комьюнити",
        "v_talk_num": "Постов: {count}",
        "v_talk_0": "Тред пуст. Будьте первым!",
        "v_talk_err": "Нет связи с тредом.",
        "v_rep_ok": "Опубликовано!",
        "v_rep_err": "Сбой запроса.",
        "v_btn_bck": "⬅️ Назад",
        "v_btn_site": "🌐 На сайт",
        "v_btn_wrt": "✍️ Написать",
        "v_rep_ask": "Отправьте текст ответом.\nОт 2 до 1800 символов.",
        "v_rep_snt": "Выгрузка...",
        "v_rep_min": "Текст слишком короткий.",
        "v_rep_max": "Превышен лимит длины.",
        "v_rep_cncl": "Отменено.",
        "v_loading_ui": "Ищем по базе Vector...",
        "v_more_replies": "...и ещё {count} ответов на сайте.",
        "v_more_comments": "...и ещё комментарии на сайте.",
        "v_upd_req": "Обновляем Vector...",
        "v_upd_ok": "Vector успешно обновлен!",
        "v_upd_err": "Ошибка обновления!",
        "v_install_log_hdr": "Журнал установки: {name}",
        "v_install_fail_forbidden": "Запрещённый метод: <code>{detail}</code>",
        "v_install_fail_requirements": "Pip-зависимости не встали: <code>{detail}</code>",
        "v_install_fail_dependency": "Не хватает зависимости: <code>{detail}</code>",
        "v_install_fail_packages": "Системные пакеты не встали: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "Пытается перезаписать ядро <code>{detail}</code>",
        "v_install_fail_ffmpeg": "Требуется ffmpeg (не установлен)",
        "v_install_fail_inline": "Требуется inline-режим (недоступен)",
        "v_install_fail_heroku_min": "Нужен Heroku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "Не найден в подключённых репозиториях",
        "v_install_fail_download": "Не удалось скачать модуль",
        "v_install_fail_unknown": "Неизвестная ошибка: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>У тебя последняя версия. Обновиться принудительно?</b>",
        "v_upd_force_btn": "🧭 Обновиться",
        "v_upd_cancel": "🚫 Отмена",
    }

    strings_jp = {
        "lang": "jp",
        "_cls_doc": "Heroku用Vectorモジュールレジストリブラウザ。",
        "v_dev_lbl": "作成者:",
        "v_dev_str": "開発:",
        "v_dev_ofc": "公式",
        "v_dev_unofc": "非公式",
        "v_info": "情報:",
        "v_cmds": "使い方:",
        "v_reqs": "ライブラリ:",
        "v_hid_cmd": "+ 非表示コマンド: {rem}。",
        "v_hid_req": "+ 非表示ライブラリ: {rem}。",
        "v_res_hdr": "見つかったモジュール:",
        "v_err_empty": "クエリを指定してください: {p}vector <テキスト>",
        "v_err_404": "次のクエリの記録はありません: {q}",
        "v_err_len": "クエリの長さは120文字に制限されています。",
        "v_err_api": "Vectorサーバーによりアクセスが拒否されました。",
        "v_ban_notice": "⛔ <b>Vectorへのアクセスはブロックされています。</b>\n<b>理由:</b> <code>{reason}</code>\n<b>期間:</b> <code>{term}</code>",
        "v_fb_add": "評価が追加されました！",
        "v_fb_rm": "評価がクリアされました！",
        "v_btn_copy": "クエリ",
        "v_btn_dl": "インストール",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "ソース",
        "v_dl_ok": "モジュールが正常にインストールされました！",
        "v_dl_err": "インストールに失敗しました！",
        "v_lim_cfg": "検索出力制限。",
        "v_btn_sec": "🛡 セキュリティスキャン",
        "v_aud_hdr": "コード監査: {name}",
        "v_aud_req": "セキュリティAPIに接続中...",
        "v_aud_proc": "ASTツリーを処理中...",
        "v_btn_aud_run": "スキャン開始",
        "v_aud_mem": "セッションキャッシュからロードされました。",
        "v_aud_lvl": "脅威レベル",
        "v_aud_stat": "スキャナデータ",
        "v_aud_out": "概要",
        "v_aud_sigs": "トリガー",
        "v_sig_crit": "クリティカル",
        "v_sig_warn": "警告",
        "v_sig_info": "通知",
        "v_aud_none": "まだスキャンされていません。1つのAPIスロットを消費します。",
        "v_aud_no_txt": "概要は生成されていません。",
        "v_aud_left": "残りスロット: {remaining}/{limit}",
        "v_aud_zero": "1日の監査制限に達しました。",
        "v_aud_err": "スキャナサーバーがダウンしています。",
        "v_err_gui": "インターフェースのレンダリングエラー。",
        "v_btn_exp": "🔽 展開",
        "v_btn_col": "🔼 折りたたむ",
        "v_btn_talk": "💬 ディスカッション",
        "v_talk_hdr": "{emoji} <b>スレッド: {name}</b>",
        "v_talk_desc": "コミュニティレビュー",
        "v_talk_num": "投稿数: {count}",
        "v_talk_0": "スレッドは空です。最初の投稿をしましょう！",
        "v_talk_err": "スレッドに接続できませんでした。",
        "v_rep_ok": "投稿されました！",
        "v_rep_err": "リクエストに失敗しました。",
        "v_btn_bck": "⬅️ 戻る",
        "v_btn_site": "🌐 Webビュー",
        "v_btn_wrt": "✍️ 返信を書く",
        "v_rep_ask": "メッセージに返信してください。\n2〜1800文字。",
        "v_rep_snt": "アップロード中...",
        "v_rep_min": "テキストが短すぎます。",
        "v_rep_max": "制限を超過しました。",
        "v_rep_cncl": "キャンセルされました。",
        "v_loading_ui": "Vectorデータベースを検索中...",
        "v_more_replies": "...サイトにはさらに{count}件の返信があります。",
        "v_more_comments": "...サイトにはさらにコメントがあります。",
        "v_upd_req": "Vectorを更新中...",
        "v_upd_ok": "Vectorが正常に更新されました！",
        "v_upd_err": "更新に失敗しました！",
        "v_install_log_hdr": "インストールログ: {name}",
        "v_install_fail_forbidden": "禁止されたメソッド: <code>{detail}</code>",
        "v_install_fail_requirements": "Pip依存関係の失敗: <code>{detail}</code>",
        "v_install_fail_dependency": "不足している依存関係: <code>{detail}</code>",
        "v_install_fail_packages": "システムパッケージの失敗: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "コアを上書きしようとしました <code>{detail}</code>",
        "v_install_fail_ffmpeg": "ffmpegが必要です（未インストール）",
        "v_install_fail_inline": "インラインモードが必要です（利用不可）",
        "v_install_fail_heroku_min": "Heroku ≥ <code>{detail}</code>が必要です",
        "v_install_fail_not_found": "設定されたリポジトリに見つかりません",
        "v_install_fail_download": "モジュールのダウンロードに失敗",
        "v_install_fail_unknown": "不明なエラー: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>最新バージョンですが、とにかくアップデートしますか？</b>",
        "v_upd_force_btn": "🧭 アップデート",
        "v_upd_cancel": "🚫 キャンセル",
    }

    strings_uk = {
        "lang": "uk",
        "_cls_doc": "Оглядач реєстру модулів Vector для Heroku.",
        "v_dev_lbl": "Автор:",
        "v_dev_str": "Розроб:",
        "v_dev_ofc": "офіц",
        "v_dev_unofc": "неофіц",
        "v_info": "Інфо:",
        "v_cmds": "Використання:",
        "v_reqs": "Бібліотеки:",
        "v_hid_cmd": "+ приховано команд: {rem}.",
        "v_hid_req": "+ приховано ліб: {rem}.",
        "v_res_hdr": "Знайдені модулі:",
        "v_err_empty": "Вкажіть запит: {p}vector <текст>",
        "v_err_404": "Немає записів за запитом: {q}",
        "v_err_len": "Довжина запиту обмежена 120 символами.",
        "v_err_api": "Відмова в доступі від сервера Vector.",
        "v_ban_notice": "⛔ <b>Доступ до Vector заблоковано.</b>\n<b>Причина:</b> <code>{reason}</code>\n<b>Термін:</b> <code>{term}</code>",
        "v_fb_add": "Оцінка додана!",
        "v_fb_rm": "Оцінка видалена!",
        "v_btn_copy": "Запит",
        "v_btn_dl": "Встановити",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "Вихідний код",
        "v_dl_ok": "Модуль успішно встановлено!",
        "v_dl_err": "Помилка встановлення!",
        "v_lim_cfg": "Ліміти виводу пошуку.",
        "v_btn_sec": "🛡 Перевірка коду",
        "v_aud_hdr": "Аудит коду: {name}",
        "v_aud_req": "З'єднання з Security API...",
        "v_aud_proc": "Аналіз AST дерева...",
        "v_btn_aud_run": "Запустити скан",
        "v_aud_mem": "Завантажено з кешу сесії.",
        "v_aud_lvl": "Рівень загрози",
        "v_aud_stat": "Дані сканера",
        "v_aud_out": "Підсумок",
        "v_aud_sigs": "Тригери",
        "v_sig_crit": "Критично",
        "v_sig_warn": "Увага",
        "v_sig_info": "Сповіщення",
        "v_aud_none": "Ще не перевірено. Витрачає 1 слот API.",
        "v_aud_no_txt": "Опис не згенеровано.",
        "v_aud_left": "Залишок слотів: {remaining}/{limit}",
        "v_aud_zero": "Добовий ліміт перевірок вичерпано.",
        "v_aud_err": "Сервер сканування недоступний.",
        "v_err_gui": "Збій рендерингу інтерфейсу.",
        "v_btn_exp": "🔽 Розгорнути",
        "v_btn_col": "🔼 Згорнути",
        "v_btn_talk": "💬 Обговорення",
        "v_talk_hdr": "{emoji} <b>Тред: {name}</b>",
        "v_talk_desc": "Відгуки спільноти",
        "v_talk_num": "Постів: {count}",
        "v_talk_0": "Тред порожній. Будьте першим!",
        "v_talk_err": "Немає зв'язку з тредом.",
        "v_rep_ok": "Опубліковано!",
        "v_rep_err": "Збій запиту.",
        "v_btn_bck": "⬅️ Назад",
        "v_btn_site": "🌐 На сайт",
        "v_btn_wrt": "✍️ Написати",
        "v_rep_ask": "Відправте текст відповіддю.\nВід 2 до 1800 символов.",
        "v_rep_snt": "Вивантаження...",
        "v_rep_min": "Текст занадто короткий.",
        "v_rep_max": "Перевищено ліміт довжини.",
        "v_rep_cncl": "Скасовано.",
        "v_loading_ui": "Шукаємо по базі Vector...",
        "v_more_replies": "...і ще {count} відповідей на сайті.",
        "v_more_comments": "...і ще коментарі на сайті.",
        "v_upd_req": "Оновлюємо Vector...",
        "v_upd_ok": "Vector успішно оновлено!",
        "v_upd_err": "Помилка оновлення!",
        "v_install_log_hdr": "Журнал встановлення: {name}",
        "v_install_fail_forbidden": "Заборонений метод: <code>{detail}</code>",
        "v_install_fail_requirements": "Pip-залежності не стали: <code>{detail}</code>",
        "v_install_fail_dependency": "Бракує залежності: <code>{detail}</code>",
        "v_install_fail_packages": "Системні пакунки не стали: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "Намагається перезаписати ядро <code>{detail}</code>",
        "v_install_fail_ffmpeg": "Потрібен ffmpeg (не встановлено)",
        "v_install_fail_inline": "Потрібен inline-режим (недоступний)",
        "v_install_fail_heroku_min": "Потрібен Heroku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "Не знайдено в підключених репозиторіях",
        "v_install_fail_download": "Не вдалося завантажити модуль",
        "v_install_fail_unknown": "Невідома помилка: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>У тебе остання версія. Оновитися примусово?</b>",
        "v_upd_force_btn": "🧭 Оновитися",
        "v_upd_cancel": "🚫 Скасувати",
    }

    strings_de = {
        "lang": "de",
        "_cls_doc": "Vector-Modul-Registry-Browser für Heroku.",
        "v_dev_lbl": "Autor:",
        "v_dev_str": "Entwickler:",
        "v_dev_ofc": "offiziell",
        "v_dev_unofc": "inoffiziell",
        "v_info": "Info:",
        "v_cmds": "Verwendung:",
        "v_reqs": "Bibliotheken:",
        "v_hid_cmd": "+ {rem} versteckte Befehle.",
        "v_hid_req": "+ {rem} versteckte Bibliotheken.",
        "v_res_hdr": "Gefundene Elemente:",
        "v_err_empty": "Suchbegriff eingeben: {p}vector <text>",
        "v_err_404": "Keine Einträge für: {q}",
        "v_err_len": "Abfragelänge ist auf 120 Zeichen begrenzt.",
        "v_err_api": "Zugriff durch Vector-Server verweigert.",
        "v_ban_notice": "⛔ <b>Zugriff auf Vector gesperrt.</b>\n<b>Grund:</b> <code>{reason}</code>\n<b>Dauer:</b> <code>{term}</code>",
        "v_fb_add": "Erfolgreich bewertet!",
        "v_fb_rm": "Bewertung gelöscht!",
        "v_btn_copy": "Abfrage",
        "v_btn_dl": "Installieren",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "Quellcode",
        "v_dl_ok": "Modul erfolgreich installiert!",
        "v_dl_err": "Installation fehlgeschlagen!",
        "v_lim_cfg": "Suchausgabe-Limits.",
        "v_btn_sec": "🛡 Sicherheits-Scan",
        "v_aud_hdr": "Code-Audit: {name}",
        "v_aud_req": "Verbindung zur Security-API...",
        "v_aud_proc": "Verarbeite AST-Baum...",
        "v_btn_aud_run": "Scan starten",
        "v_aud_mem": "Aus dem Session-Cache geladen.",
        "v_aud_lvl": "Bedrohungsstufe",
        "v_aud_stat": "Scanner-Daten",
        "v_aud_out": "Zusammenfassung",
        "v_aud_sigs": "Auslöser",
        "v_sig_crit": "Kritisch",
        "v_sig_warn": "Warnungen",
        "v_sig_info": "Hinweise",
        "v_aud_none": "Noch nicht gescannt. Verbraucht 1 API-Slot.",
        "v_aud_no_txt": "Keine Zusammenfassung generiert.",
        "v_aud_left": "Verbleibende Slots: {remaining}/{limit}",
        "v_aud_zero": "Tägliches Audit-Limit aufgebraucht.",
        "v_aud_err": "Scanner-Server ist offline.",
        "v_err_gui": "Fehler beim Rendern der Benutzeroberfläche.",
        "v_btn_exp": "🔽 Erweitern",
        "v_btn_col": "🔼 Zuklappen",
        "v_btn_talk": "💬 Diskussion",
        "v_talk_hdr": "{emoji} <b>Thread: {name}</b>",
        "v_talk_desc": "Community-Bewertungen",
        "v_talk_num": "Beiträge: {count}",
        "v_talk_0": "Der Thread ist leer. Sei der Erste!",
        "v_talk_err": "Keine Verbindung zum Thread.",
        "v_rep_ok": "Gepostet!",
        "v_rep_err": "Anfrage fehlgeschlagen.",
        "v_btn_bck": "⬅️ Zurück",
        "v_btn_site": "🌐 Web-Ansicht",
        "v_btn_wrt": "✍️ Antworten",
        "v_rep_ask": "Auf Beitrag antworten.\n2-1800 Zeichen.",
        "v_rep_snt": "Wird hochgeladen...",
        "v_rep_min": "Text ist zu kurz.",
        "v_rep_max": "Limit überschritten.",
        "v_rep_cncl": "Abgebrochen.",
        "v_loading_ui": "Durchsuche Vector-Datenbank...",
        "v_more_replies": "...und {count} weitere Antworten auf der Seite.",
        "v_more_comments": "...und weitere Kommentare auf der Seite.",
        "v_upd_req": "Vector wird aktualisiert...",
        "v_upd_ok": "Vector erfolgreich aktualisiert!",
        "v_upd_err": "Aktualisierung fehlgeschlagen!",
        "v_install_log_hdr": "Installationsprotokoll: {name}",
        "v_install_fail_forbidden": "Verbotene Methode: <code>{detail}</code>",
        "v_install_fail_requirements": "Pip-Abhängigkeiten fehlgeschlagen: <code>{detail}</code>",
        "v_install_fail_dependency": "Fehlende Abhängigkeit: <code>{detail}</code>",
        "v_install_fail_packages": "Systempakete fehlgeschlagen: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "Versucht Kern <code>{detail}</code> zu überschreiben",
        "v_install_fail_ffmpeg": "Benötigt ffmpeg (nicht installiert)",
        "v_install_fail_inline": "Benötigt Inline-Modus (nicht verfügbar)",
        "v_install_fail_heroku_min": "Benötigt Heroku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "Nicht in konfigurierten Repos gefunden",
        "v_install_fail_download": "Modul-Download fehlgeschlagen",
        "v_install_fail_unknown": "Unbekannter Fehler: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>Du hast bereits die neueste Version. Trotzdem aktualisieren?</b>",
        "v_upd_force_btn": "🧭 Aktualisieren",
        "v_upd_cancel": "🚫 Abbrechen",
    }

    strings_neofit = {
        "lang": "neofit",
        "_cls_doc": "Vector module registry browser for Heroku.",
        "v_dev_lbl": "by",
        "v_dev_str": "dev",
        "v_dev_ofc": "verified",
        "v_dev_unofc": "3rd-party",
        "v_info": "info",
        "v_cmds": "usage",
        "v_reqs": "deps",
        "v_hid_cmd": "+ {rem} hidden cmds.",
        "v_hid_req": "+ {rem} hidden deps.",
        "v_res_hdr": "stdout:",
        "v_err_empty": "<b>SyntaxError:</b> missing query. <code>{p}vector &lt;text&gt;</code>",
        "v_err_404": "<b>grep:</b> <code>{q}</code> not found.",
        "v_err_len": "<b>Buffer overflow:</b> max 120 chars.",
        "v_err_api": "<b>403 Forbidden</b> by Vector API.",
        "v_ban_notice": "⛔ <b>Vector blocked access.</b>\n<b>rule:</b> <code>{reason}</code>\n<b>TTL:</b> <code>{term}</code>",
        "v_fb_add": "Rated.",
        "v_fb_rm": "Rating cleared.",
        "v_btn_copy": "query",
        "v_btn_dl": "install",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "src",
        "v_dl_ok": "Installed.",
        "v_dl_err": "Install failed.",
        "v_lim_cfg": "Search output limits.",
        "v_btn_sec": "🛡 Security scan",
        "v_aud_hdr": "Code audit: {name}",
        "v_aud_req": "Connecting to security API...",
        "v_aud_proc": "Parsing AST...",
        "v_btn_aud_run": "Run scan",
        "v_aud_mem": "Loaded from cache.",
        "v_aud_lvl": "Threat level",
        "v_aud_stat": "Scanner data",
        "v_aud_out": "Summary",
        "v_aud_sigs": "Signals",
        "v_sig_crit": "SIGKILL",
        "v_sig_warn": "SIGTERM",
        "v_sig_info": "SIGUSR1",
        "v_aud_none": "Not scanned yet. Uses 1 API slot.",
        "v_aud_no_txt": "No summary generated.",
        "v_aud_left": "Slots: {remaining}/{limit}",
        "v_aud_zero": "Daily limit exhausted.",
        "v_aud_err": "Scanner server is down.",
        "v_err_gui": "GUI render error.",
        "v_btn_exp": "🔽 Expand",
        "v_btn_col": "🔼 Collapse",
        "v_btn_talk": "💬 Discussion",
        "v_talk_hdr": "{emoji} <b>Thread: {name}</b>",
        "v_talk_desc": "Community reviews",
        "v_talk_num": "Posts: {count}",
        "v_talk_0": "Thread is empty. Be the first!",
        "v_talk_err": "Connection refused.",
        "v_rep_ok": "Posted.",
        "v_rep_err": "Request failed.",
        "v_btn_bck": "⬅️ Back",
        "v_btn_site": "🌐 Web",
        "v_btn_wrt": "✍️ Reply",
        "v_rep_ask": "Reply to post.\n2–1800 chars.",
        "v_rep_snt": "Uploading...",
        "v_rep_min": "Too short.",
        "v_rep_max": "Limit exceeded.",
        "v_rep_cncl": "Cancelled.",
        "v_loading_ui": "Searching Vector database...",
        "v_more_replies": "...and {count} more replies.",
        "v_more_comments": "...and more comments.",
        "v_upd_req": "Updating Vector...",
        "v_upd_ok": "Updated.",
        "v_upd_err": "Update failed.",
        "v_install_log_hdr": "install log: {name}",
        "v_install_fail_forbidden": "forbidden method: <code>{detail}</code>",
        "v_install_fail_requirements": "pip deps failed: <code>{detail}</code>",
        "v_install_fail_dependency": "missing dep: <code>{detail}</code>",
        "v_install_fail_packages": "system pkgs failed: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "core overwrite attempt: <code>{detail}</code>",
        "v_install_fail_ffmpeg": "needs ffmpeg (not found)",
        "v_install_fail_inline": "needs inline mode (dead)",
        "v_install_fail_heroku_min": "needs Heroku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "not in configured repos",
        "v_install_fail_download": "download failed",
        "v_install_fail_unknown": "unknown error: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>Up to date. git pull --force?</b>",
        "v_upd_force_btn": "🧭 git pull",
        "v_upd_cancel": "🚫 abort",
    }

    strings_tiktok = {
        "lang": "tiktok",
        "_cls_doc": "Темка для поиска модулей Vector под Heroku.",
        "v_dev_lbl": "Кодер:",
        "v_dev_str": "дев:",
        "v_dev_ofc": "офиц",
        "v_dev_unofc": "ноунэйм",
        "v_info": "Инфа:",
        "v_cmds": "Команды:",
        "v_reqs": "Либы:",
        "v_hid_cmd": "+ заныкано: {rem}",
        "v_hid_req": "+ заныкано либ: {rem}",
        "v_res_hdr": "Нашлось:",
        "v_err_empty": "Чё искать-то? Пиши: {p}vector <текст>",
        "v_err_404": "Пусто по запросу: {q}",
        "v_err_len": "Длинновато, до 120 симв.",
        "v_err_api": "Сервер Vector не пускает.",
        "v_ban_notice": "⛔ <b>Вектор тебя забанил.</b>\n<b>Причина:</b> <code>{reason}</code>\n<b>Срок:</b> <code>{term}</code>",
        "v_fb_add": "Лайк влеплен!",
        "v_fb_rm": "Лайк снят!",
        "v_btn_copy": "Запрос",
        "v_btn_dl": "Поставить",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "Код",
        "v_dl_ok": "Поставилось!",
        "v_dl_err": "Не встало!",
        "v_lim_cfg": "Лимиты выдачи.",
        "v_btn_sec": "🛡 Чек кода",
        "v_aud_hdr": "Прожарка: {name}",
        "v_aud_req": "Стучимся в API защиты...",
        "v_aud_proc": "Парсим AST...",
        "v_btn_aud_run": "Скан",
        "v_aud_mem": "Из кэша.",
        "v_aud_lvl": "Кринжометр",
        "v_aud_stat": "Дата",
        "v_aud_out": "Итог",
        "v_aud_sigs": "Редфлаги",
        "v_sig_crit": "Жёстко",
        "v_sig_warn": "Аккуратно",
        "v_sig_info": "Инфа",
        "v_aud_none": "Ещё не чекали. Жрёт 1 слот.",
        "v_aud_no_txt": "Пусто.",
        "v_aud_left": "Слотов: {remaining}/{limit}",
        "v_aud_zero": "Лимит на сегодня всё.",
        "v_aud_err": "Чекер лёг.",
        "v_err_gui": "Интерфейс крашнулся.",
        "v_btn_exp": "🔽 Открыть",
        "v_btn_col": "🔼 Закрыть",
        "v_btn_talk": "💬 Курилка",
        "v_talk_hdr": "{emoji} <b>Курилка: {name}</b>",
        "v_talk_desc": "Чё пишут люди",
        "v_talk_num": "Постов: {count}",
        "v_talk_0": "Пусто. Будь первым!",
        "v_talk_err": "Связи нет.",
        "v_rep_ok": "Улетело!",
        "v_rep_err": "Фейл.",
        "v_btn_bck": "⬅️ Назад",
        "v_btn_site": "🌐 Сайт",
        "v_btn_wrt": "✍️ Ответ",
        "v_rep_ask": "Реплай на сообщение.\nОт 2 до 1800 симв.",
        "v_rep_snt": "Пушим...",
        "v_rep_min": "Мало букав.",
        "v_rep_max": "Дохрена букав.",
        "v_rep_cncl": "Забили.",
        "v_loading_ui": "Ищем по базе Vector...",
        "v_more_replies": "...и ещё {count} комментов.",
        "v_more_comments": "...и ещё спам на сайте.",
        "v_upd_req": "Качаем обнову...",
        "v_upd_ok": "Обнова залетела!",
        "v_upd_err": "Не обновилось!",
        "v_install_log_hdr": "Лог установки: {name}",
        "v_install_fail_forbidden": "Запрещёнка: <code>{detail}</code>",
        "v_install_fail_requirements": "Пип-либы не встали: <code>{detail}</code>",
        "v_install_fail_dependency": "Не хватает: <code>{detail}</code>",
        "v_install_fail_packages": "Системные пакеты мимо: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "Лезет в ядро <code>{detail}</code>",
        "v_install_fail_ffmpeg": "Нужен ffmpeg (нету)",
        "v_install_fail_inline": "Нужен inline (не раб)",
        "v_install_fail_heroku_min": "Нужен Heroku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "Нет в подключённых репах",
        "v_install_fail_download": "Не скачалось",
        "v_install_fail_unknown": "Непонятная ошибка: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>У тебя ласт версия. Все равно обновить?</b>",
        "v_upd_force_btn": "🧭 Обнова",
        "v_upd_cancel": "🚫 Отбой",
    }

    strings_leet = {
        "lang": "leet",
        "_cls_doc": "V3c70r m0dul3 r3g157ry br0ws3r f0r H3r0ku.",
        "v_dev_lbl": "4u7h0r:",
        "v_dev_str": "d3v:",
        "v_dev_ofc": "0ff1c14l",
        "v_dev_unofc": "un0ff1c14l",
        "v_info": "1nf0:",
        "v_cmds": "U54g3:",
        "v_reqs": "L1b5:",
        "v_hid_cmd": "+ {rem} h1dd3n cmd5.",
        "v_hid_req": "+ {rem} h1dd3n l1b5.",
        "v_res_hdr": "F0und:",
        "v_err_empty": "N33d qu3ry: {p}v3c70r <73x7>",
        "v_err_404": "N0 r3c0rd5 f0r: {q}",
        "v_err_len": "Qu3ry 700 l0ng (120 ch4r5 m4x).",
        "v_err_api": "4cc355 d3n13d by V3c70r 53rv3r.",
        "v_ban_notice": "⛔ <b>V3c70r 4cc355 bl0ck3d.</b>\n<b>R3450n:</b> <code>{reason}</code>\n<b>73rm:</b> <code>{term}</code>",
        "v_fb_add": "R473d!",
        "v_fb_rm": "R471ng cl34r3d!",
        "v_btn_copy": "Qu3ry",
        "v_btn_dl": "1n574ll",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "50urc3",
        "v_dl_ok": "1n574ll3d!",
        "v_dl_err": "F41l3d!",
        "v_lim_cfg": "534rch l1m175.",
        "v_btn_sec": "🛡 53cur17y 5c4n",
        "v_aud_hdr": "C0d3 4ud17: {name}",
        "v_aud_req": "C0nn3c71ng 70 53cur17y 4P1...",
        "v_aud_proc": "Pr0c3551ng A57 7r33...",
        "v_btn_aud_run": "574r7 5c4n",
        "v_aud_mem": "L04d3d fr0m c4ch3.",
        "v_aud_lvl": "7hr347 L3v3l",
        "v_aud_stat": "5c4nn3r D474",
        "v_aud_out": "5umm4ry",
        "v_aud_sigs": "7r1gg3r5",
        "v_sig_crit": "Cr171c4l",
        "v_sig_warn": "W4rn1ng5",
        "v_sig_info": "N071c35",
        "v_aud_none": "N07 5c4nn3d y37. C0575 1 4P1 5l07.",
        "v_aud_no_txt": "N0 5umm4ry.",
        "v_aud_left": "5l075 l3f7: {remaining}/{limit}",
        "v_aud_zero": "4ud17 l1m17 d3pl373d.",
        "v_aud_err": "5c4nn3r 53rv3r d0wn.",
        "v_err_gui": "GU1 3rr0r.",
        "v_btn_exp": "🔽 3xp4nd",
        "v_btn_col": "🔼 C0ll4p53",
        "v_btn_talk": "💬 D15cu55",
        "v_talk_hdr": "{emoji} <b>7hr34d: {name}</b>",
        "v_talk_desc": "C0mmun17y r3v13w5",
        "v_talk_num": "P0575: {count}",
        "v_talk_0": "7hr34d 15 3mp7y. B3 f1r57!",
        "v_talk_err": "C4n'7 c0nn3c7.",
        "v_rep_ok": "P0573d!",
        "v_rep_err": "R3qu357 f41l3d.",
        "v_btn_bck": "⬅️ B4ck",
        "v_btn_site": "🌐 W3b",
        "v_btn_wrt": "✍️ R3ply",
        "v_rep_ask": "R3ply 70 p057.\n2-1800 ch4r5.",
        "v_rep_snt": "Upl04d1ng...",
        "v_rep_min": "700 5h0r7.",
        "v_rep_max": "L1m17 3xc33d3d.",
        "v_rep_cncl": "C4nc3ll3d.",
        "v_loading_ui": "534rch1ng V3c70r d474b453...",
        "v_more_replies": "...4nd {count} m0r3 r3pl135.",
        "v_more_comments": "...4nd m0r3 c0mm3n75.",
        "v_upd_req": "Upd471ng V3c70r...",
        "v_upd_ok": "V3c70r upd473d!",
        "v_upd_err": "Upd473 f41l3d!",
        "v_install_log_hdr": "1n574ll l0g: {name}",
        "v_install_fail_forbidden": "f0rb1dd3n m37h0d: <code>{detail}</code>",
        "v_install_fail_requirements": "p1p d3p5 f41l3d: <code>{detail}</code>",
        "v_install_fail_dependency": "m1551n9 d3p: <code>{detail}</code>",
        "v_install_fail_packages": "pkg5 f41l3d: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "c0r3 0v3rwr173: <code>{detail}</code>",
        "v_install_fail_ffmpeg": "n33d5 ffmp39 (n07 f0und)",
        "v_install_fail_inline": "n33d5 1nl1n3 (d34d)",
        "v_install_fail_heroku_min": "n33d5 H3r0ku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "n07 1n c0nf16'd r3p05",
        "v_install_fail_download": "d0wnl04d f41l3d",
        "v_install_fail_unknown": "unkn0wn 3rr: <code>{detail}</code>",
        "v_upd_same": "🌟 <b>U r 0n 7h3 l47357 v3r510n, pull upd4735 4nyw4y?</b>",
        "v_upd_force_btn": "🧭 Upd473",
        "v_upd_cancel": "🚫 n0p3",
    }

    strings_uwu = {
        "lang": "uwu",
        "_cls_doc": "Vectow moduwe wegistwy bwowsew fow Hewoku >w<",
        "v_dev_lbl": "Authow:",
        "v_dev_str": "dev:",
        "v_dev_ofc": "officiaw",
        "v_dev_unofc": "unofficiaw",
        "v_info": "Info:",
        "v_cmds": "Usage:",
        "v_reqs": "Wibs:",
        "v_hid_cmd": "+ {rem} hidden cmds.",
        "v_hid_req": "+ {rem} hidden wibs.",
        "v_res_hdr": "Found owo:",
        "v_err_empty": "hewwo pws specify quewy: {p}vectow <text>",
        "v_err_404": "N-No wecowds fow: {q} T_T",
        "v_err_len": "Quewy too wong (120 chaws) >_<",
        "v_err_api": "Access denied by Vectow Sewvew qwq.",
        "v_ban_notice": "⛔ <b>Vectow bwocked access.</b>\n<b>Weason:</b> <code>{reason}</code>\n<b>Tewm:</b> <code>{term}</code>",
        "v_fb_add": "Wated! (≧◡≦)",
        "v_fb_rm": "Wating cweawed ;w;",
        "v_btn_copy": "Quewy",
        "v_btn_dl": "Instaww",
        "v_page": "[{idx}/{total}]",
        "v_btn_code": "Souwce",
        "v_dl_ok": "Instawwed! (≧◡≦)",
        "v_dl_err": "Instaww faiwed! ;w;",
        "v_lim_cfg": "Seawch wimits.",
        "v_btn_sec": "🛡 Secuwity Scan",
        "v_aud_hdr": "Code Audit: {name}",
        "v_aud_req": "Connecting to Secuwity API...",
        "v_aud_proc": "Pwocessing AST twee...",
        "v_btn_aud_run": "Stawt Scan",
        "v_aud_mem": "Woaded fwom cache.",
        "v_aud_lvl": "Thweat Wevew",
        "v_aud_stat": "Scannew Data",
        "v_aud_out": "Summawy",
        "v_aud_sigs": "Twiggews",
        "v_sig_crit": "Cwiticaw",
        "v_sig_warn": "Wawnings",
        "v_sig_info": "Notices",
        "v_aud_none": "Not scanned yet. Takes 1 API swot.",
        "v_aud_no_txt": "No summawy gwenerated.",
        "v_aud_left": "Swots weft: {remaining}/{limit}",
        "v_aud_zero": "Daiwy wimit depweted T_T.",
        "v_aud_err": "Scannew sewvew down qwq.",
        "v_err_gui": "GUI ewwow >_<.",
        "v_btn_exp": "🔽 Expand",
        "v_btn_col": "🔼 Cowwapse",
        "v_btn_talk": "💬 Discussion",
        "v_talk_hdr": "{emoji} <b>Thwead: {name}</b>",
        "v_talk_desc": "Community weviews",
        "v_talk_num": "Posts: {count}",
        "v_talk_0": "Thwead is empty. Be fiwst! >w<",
        "v_talk_err": "Couwdn't connect to thwead.",
        "v_rep_ok": "Posted! (≧◡≦)",
        "v_rep_err": "Wequest faiwed T_T.",
        "v_btn_bck": "⬅️ Back",
        "v_btn_site": "🌐 Web View",
        "v_btn_wrt": "✍️ Wepwy",
        "v_rep_ask": "Wepwy to post.\n2-1800 chaws uwu.",
        "v_rep_snt": "Upwoading...",
        "v_rep_min": "Text too showt.",
        "v_rep_max": "Wimit exceeded.",
        "v_rep_cncl": "Cancewwed.",
        "v_loading_ui": "Seawching Vectow database...",
        "v_more_replies": "...and {count} mowe wepwies on site.",
        "v_more_comments": "...and mowe comments on site.",
        "v_upd_req": "Updating Vectow...",
        "v_upd_ok": "Vectow updated! (≧◡≦)",
        "v_upd_err": "Update faiwed! ;w;",
        "v_install_log_hdr": "Instaww wog: {name} >w<",
        "v_install_fail_forbidden": "Fowbidden method: <code>{detail}</code> ;(",
        "v_install_fail_requirements": "Pip deps faiwed: <code>{detail}</code> owo",
        "v_install_fail_dependency": "Missing dep: <code>{detail}</code> ;;w;;",
        "v_install_fail_packages": "System pkgs faiwed: <code>{detail}</code>",
        "v_install_fail_core_overwrite": "Twied to ovewwwite cowe <code>{detail}</code>",
        "v_install_fail_ffmpeg": "Needs ffmpeg (not instawwed) uwu",
        "v_install_fail_inline": "Needs inwine mode (unavaiwabwe)",
        "v_install_fail_heroku_min": "Needs Hewoku ≥ <code>{detail}</code>",
        "v_install_fail_not_found": "Not found in wepos ;w;",
        "v_install_fail_download": "Downwoad faiwed owo",
        "v_install_fail_unknown": "Unknown ewwow: <code>{detail}</code> >~<",
        "v_upd_same": "🌟 <b>You awe on da watest vewsion, puww updates anyway? (´• ω •`)</b>",
        "v_upd_force_btn": "🧭 Puww Update",
        "v_upd_cancel": "🚫 Nu ;-;",
    }

    def _detect_lang_suffix(self) -> str:
        variants = {"en", "ru", "jp", "uk", "de", "neofit", "tiktok", "leet", "uwu"}
        lang = str(self.strings.get("lang", "en")).strip().lower()
        return lang if lang in variants else "en"


    ICONS = {
        "search": '<tg-emoji emoji-id="5447459604524971717">🔎</tg-emoji>',
        "error": '<tg-emoji emoji-id="5388785832956016892">❌</tg-emoji>',
        "warn": '<tg-emoji emoji-id="5881702736843511327">⚠️</tg-emoji>',
        "description": '<tg-emoji emoji-id="6008090211181923982">📝</tg-emoji>',
        "command": '<tg-emoji emoji-id="5877260593903177342">⚙</tg-emoji>',
        "dependency": '<tg-emoji emoji-id="5325732612084351248">📦</tg-emoji>',
        "module": '<tg-emoji emoji-id="5924720918826848520">📦</tg-emoji>',
        "modules_list": '<tg-emoji emoji-id="5883973610606956186">🗂</tg-emoji>',
        "shield": '<tg-emoji emoji-id="5926783847453692661">🛡</tg-emoji>',
        "safe": '<tg-emoji emoji-id="5776375003280838798">✅</tg-emoji>',
        "unsafe": '<tg-emoji emoji-id="5778527486270770928">❌</tg-emoji>',
        "stats": '<tg-emoji emoji-id="5877485980901971030">📊</tg-emoji>',
        "quota": '<tg-emoji emoji-id="6311858554944888333">⌚️</tg-emoji>',
        "verified": '<tg-emoji emoji-id="5958376256788502078">⭐️</tg-emoji>',
        "comments": '<tg-emoji emoji-id="5886666250158870040">💬</tg-emoji>',
        "reply": "↳",
        "broken": '<tg-emoji emoji-id="5877260593903177342">💥</tg-emoji>',
        "globe": '<tg-emoji emoji-id="5877485980901971030">🌐</tg-emoji>',
    }

    _INSTALL_ERR_PATTERNS = [
        ("forbidden", re.compile(r"uses forbidden method:\s*(.+)")),
        ("requirements", re.compile(r"requirements.*failed to install:\s*(.+)", re.DOTALL)),
        ("dependency", re.compile(r"requires missing dependency\s+(.+)")),
        ("packages", re.compile(r"system packages.*failed to install:\s*(.+)", re.DOTALL)),
        ("core_overwrite", re.compile(r"tried to overwrite core\s+(\S+)\s+(\S+)")),
        ("ffmpeg", re.compile(r"requires ffmpeg")),
        ("inline", re.compile(r"requires inline mode")),
        ("heroku_min", re.compile(r"requires Heroku\s+(\S+),\s*current version is\s+(\S+)")),
        ("not_found", re.compile(r"was not found in configured repos")),
        ("download", re.compile(r"Failed to download module")),
    ]

    class _InstallLogCapture(logging.Handler):
        def __init__(self):
            super().__init__()
            self.records: List[logging.LogRecord] = []

        def emit(self, record: logging.LogRecord) -> None:
            self.records.append(record)

    def _classify_install_errors(self, records: List[logging.LogRecord]) -> List[Dict[str, str]]:
        errors = []
        for rec in records:
            if rec.levelno < logging.WARNING:
                continue
            msg = rec.getMessage()
            for err_type, pattern in self._INSTALL_ERR_PATTERNS:
                m = pattern.search(msg)
                if m:
                    if err_type == "core_overwrite":
                        detail = f"{m.group(1)}.{m.group(2)}"
                    elif err_type == "heroku_min":
                        detail = f"{m.group(1)} (current: {m.group(2)})"
                    elif m.lastindex:
                        detail = m.group(1).strip()
                    else:
                        detail = ""
                    errors.append({"type": err_type, "detail": detail, "raw": msg})
                    break
            else:
                if rec.levelno >= logging.ERROR:
                    errors.append({"type": "unknown", "detail": msg[:200], "raw": msg})
        return errors

    def _fmt_install_errors(self, m_name: str, errors: List[Dict[str, str]]) -> str:
        if not errors:
            return f"{self.ICONS['error']} <b>{self.strings['v_dl_err']}</b>"

        lines = [f"{self.ICONS['broken']} <b>{self.strings['v_install_log_hdr'].format(name=m_name)}</b>"]
        seen = set()
        for err in errors:
            key = err["type"]
            if key in seen:
                continue
            seen.add(key)
            detail = err["detail"]
            str_key = f"v_install_fail_{key}"
            fmt = self.strings.get(str_key)
            if fmt:
                try:
                    lines.append(f"{self.ICONS['warn']} {fmt.format(detail=detail)}")
                except (KeyError, ValueError):
                    lines.append(f"{self.ICONS['warn']} {fmt}")
            else:
                lines.append(f"{self.ICONS['warn']} {detail or err['raw'][:200]}")

        return "\n".join(lines)

    async def _safe_install(self, m_name: str, dl_url: str, *, notify: bool = True) -> tuple:
        ldr = self.lookup("Loader")
        if not ldr or not hasattr(ldr, "download_and_install"):
            return -1, []

        cap = self._InstallLogCapture()
        cap.setLevel(logging.WARNING)
        for lg_name in ("heroku.modules.loader", "heroku", ""):
            logging.getLogger(lg_name).addHandler(cap)

        classified = []
        try:
            res = await ldr.download_and_install(dl_url)
            if getattr(ldr, "fully_loaded", False):
                ldr.update_modules_in_db()
            return res, classified
        except Exception as e:
            log.warning("Install wrapper caught exception for %s: %r", m_name, e)
            return 0, classified
        finally:
            for lg_name in ("heroku.modules.loader", "heroku", ""):
                logging.getLogger(lg_name).removeHandler(cap)
            if cap.records:
                classified = self._classify_install_errors(cap.records)
                if notify and classified:
                    log.info("Install errors for %s: %s", m_name, [e["type"] for e in classified])

    def __init__(self) -> None:
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "limit", 
                30, 
                lambda: self.strings("v_lim_cfg"), 
                validator=loader.validators.Integer(minimum=1, maximum=100)
            )
        )
        self.http: Optional[aiohttp.ClientSession] = None
        self._security_cache: Dict[str, Dict[str, Any]] = {}
        self._last_http_code = 0
        self._last_ban_notice = ""

    async def client_ready(self, client: "herokutl.TelegramClient", database: "loader.Database") -> None:
        self.client = client
        self.database = database
        self.http = aiohttp.ClientSession()
        
        log.info("Vector Module Monolith Started")

    async def on_unload(self) -> None:
        if self.http and not self.http.closed:
            await self.http.close()

    async def _net_req(self, method: str, path: str, token: str = "", params: dict = None, json_data: dict = None, as_bytes: bool = False, timeout: int = 15) -> Any:
        if not self.http or self.http.closed:
            self.http = aiohttp.ClientSession()
            
        url = urljoin(API_ROOT + "/", path.lstrip("/"))
        headers = {"User-Agent": "VectorUserbotClient/2.0"}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        self._last_http_code = 0
        try:
            async with self.http.request(method, url, params=params, json=json_data, headers=headers, timeout=aiohttp.ClientTimeout(total=timeout)) as r:
                self._last_http_code = r.status
                log.debug("HTTP %s %s -> %s", method, path, r.status)
                if r.status >= 300:
                    return None
                if as_bytes:
                    return await r.read()
                return await r.json(content_type=None)
        except Exception as e:
            log.warning("HTTP request failed method=%s path=%s error=%r", method, path, e)
            return None

    def _normalize_module(self, raw: dict) -> dict:
        cmds = []
        for c in (raw.get("commands") or []):
            if isinstance(c, dict):
                cmds.append({
                    "name": c.get("name") or c.get("cmd") or "",
                    "description": c.get("description") or c.get("desc") or ""
                })

        dev = str(raw.get("developer") or raw.get("author") or "@Unknown")
        clean_dev = dev.strip().lower().lstrip('@')
        is_official = bool(
            raw.get("official") 
            or raw.get("is_official") 
            or raw.get("verified") 
            or raw.get("is_verified") 
            or raw.get("telegram_verified") 
            or raw.get("official_developer") 
            or raw.get("is_official_developer") 
            or clean_dev in {"goymodules", "samsepi0l_ovf"}
        )
        name = str(raw.get("name") or raw.get("class_name") or "Unknown")
        
        return {
            "name": name,
            "version": raw.get("version") or "?.?.?",
            "author": dev,
            "description": raw.get("description") or "",
            "commands": cmds,
            "dependencies": [str(d) for d in (raw.get("dependencies") or [])],
            "official": is_official,
            "likes": int(raw.get("likes") or 0),
            "dislikes": int(raw.get("dislikes") or 0),
            "banner": raw.get("banner"),
            "source_url": raw.get("source_url") or f"{API_ROOT}/modules/{quote(name, safe='')}/source",
            "dl_url": raw.get("source_url") or f"{API_ROOT}/modules/{quote(name, safe='')}/source",
        }

    @staticmethod
    def _extract_counts(data: dict):
        likes = dislikes = None
        for container in (data, data.get("module"), data.get("data"), data.get("result"), data.get("summary")):
            if not isinstance(container, dict):
                continue
            for lk in ("likes", "likes_count", "likesCount", "likeCount", "like_count"):
                v = container.get(lk)
                if v is not None:
                    try:
                        likes = int(v)
                    except (ValueError, TypeError):
                        pass
                    break
            for dk in ("dislikes", "dislikes_count", "dislikesCount", "dislikeCount", "dislike_count"):
                v = container.get(dk)
                if v is not None:
                    try:
                        dislikes = int(v)
                    except (ValueError, TypeError):
                        pass
                    break
            if likes is not None and dislikes is not None:
                break
        return likes, dislikes

    def _parse_jwt(self, token: str) -> dict:
        try:
            b64_part = token.split(".")[1]
            b64_part += "=" * (-len(b64_part) % 4)
            return json.loads(base64.urlsafe_b64decode(b64_part.encode()).decode())
        except Exception:
            return {}

    @staticmethod
    def _norm_hash_name(value: str) -> str:
        value = unicodedata.normalize("NFKC", str(value or ""))
        value = value.replace("​", "").replace("‌", "").replace("‍", "").replace("﻿", "")
        return " ".join(value.strip().split())

    async def _get_active_token(self, force: bool = False) -> str:
        if force:
            self.set("auth_token", None)
            
        cached = self.get("auth_token")
        if cached:
            payload = self._parse_jwt(cached)
            if payload.get("exp", 0) - time.time() > 60:
                return cached

        bot_info = await self._net_req("GET", "/api/tg-bot")
        bot_username = (bot_info or {}).get("username", "").strip().lstrip("@")
        if not bot_username:
            log.warning("No bot username returned from /api/tg-bot")
            return ""

        me = await self.client.get_me()
        uid = str(getattr(me, "id", ""))
        uname = getattr(me, "username", "") or ""
        fname = getattr(me, "first_name", "") or ""
        lname = getattr(me, "last_name", "") or ""
        dname = " ".join(filter(None, [fname, lname])).strip() or uname or uid

        uname = self._norm_hash_name(uname).lower()
        dname = self._norm_hash_name(dname)

        with suppress(Exception):
            await self.client(UnblockRequest(bot_username))

        new_jwt = ""
        ban_notice = ""
        for attempt in range(2):
            b_stamp = int(time.time() // 10) - attempt
            cmd_hash = hashlib.sha256(f"vector-token-v2|{uid}|{b_stamp}|{AUTH_SALT}".encode()).hexdigest()[:32]
            cmd_str = f"/{cmd_hash}"

            try:
                async with self.client.conversation(bot_username, timeout=12, exclusive=False) as conv:
                    out_msg = await conv.send_message(cmd_str)
                    try:
                        resp = await asyncio.wait_for(conv.get_response(), timeout=10)
                        txt = getattr(resp, "raw_text", getattr(resp, "text", ""))
                        match = JWT_REGEX.search(txt)
                        if match:
                            new_jwt = match.group(0)
                        elif "заблок" in txt.lower() or "⛔" in txt:
                            ban_notice = self._format_ban_notice(txt)
                        with suppress(Exception): await out_msg.delete()
                        if new_jwt: break
                    except asyncio.TimeoutError:
                        with suppress(Exception): await out_msg.delete()
            except Exception as e:
                log.warning("Token conversation attempt=%s failed: %r", attempt, e)

        if new_jwt:
            self.set("auth_token", new_jwt)
            self._last_ban_notice = ""
        elif ban_notice:
            self._last_ban_notice = ban_notice
        return new_jwt

    def _format_ban_notice(self, raw_text: str) -> str:
        txt = str(raw_text or "").strip()
        reason_match = BAN_REASON_RE.search(txt)
        term_match = BAN_TERM_RE.search(txt)

        reason_raw = reason_match.group(1).strip() if reason_match else ""
        term_raw = term_match.group(1).strip() if term_match else ""

        if not reason_raw or not term_raw:
            for line in txt.splitlines():
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                key_l = key.strip().lower()
                val = value.strip()
                if not reason_raw and key_l in {"причина", "reason", "理由", "grund", "r3450n", "weason", "charge"}:
                    reason_raw = val
                if not term_raw and key_l in {"срок", "term", "期間", "dauer", "73rm", "tewm"}:
                    term_raw = val

        reason = utils.escape_html(reason_raw or "-")
        term = utils.escape_html(term_raw or "permanent")
        return self.strings["v_ban_notice"].format(reason=reason, term=term)

    def _build_html(self, m_data: dict, current_idx: int, total_cnt: int) -> str:
        name = utils.escape_html(str(m_data.get("name", "Unknown")))
        author = utils.escape_html(str(m_data.get("author", "@Unknown")))
        ver = str(m_data.get("version", "?.?.?"))
        
        lines = [f"{self.ICONS['module']} <code>{name}</code> <b>{self.strings['v_dev_lbl']}</b> <code>{author}</code>"]
        if ver != "?.?.?":
            lines[-1] += f" (<code>v{utils.escape_html(ver)}</code>)"
            
        status = self.strings["v_dev_ofc"] if m_data.get("official") else self.strings["v_dev_unofc"]
        lines.append(f"{self.ICONS['verified']} <b>{self.strings['v_dev_str']}</b> <code>{status}</code>")
        if total_cnt > 1:
            lines.append(f"{self.ICONS['modules_list']} <i>{self.strings['v_page'].format(idx=current_idx, total=total_cnt)}</i>")
            
        desc = m_data.get("description")
        if desc:
            lines.append(f"\n{self.ICONS['description']} <b>{self.strings['v_info']}</b>\n<blockquote expandable>{utils.escape_html(str(desc))}</blockquote>")
            
        doc_str = "\n".join(lines)
        
        cmds = m_data.get("commands", [])
        if cmds:
            c_lines = []
            for i, c in enumerate(cmds):
                cn = utils.escape_html(str(c.get("name", "")))
                cd = utils.escape_html(str(c.get("description", ""))).split("\n")[0]
                c_lines.append(f"<code>{self.get_prefix()}{cn}</code> {cd}")
            doc_str += f"\n\n{self.ICONS['command']} <b>{self.strings['v_cmds']}</b>\n<blockquote expandable>{chr(10).join(c_lines)}</blockquote>"

        deps = m_data.get("dependencies", [])
        if deps:
            d_lines = [f"<code>{utils.escape_html(d)}</code>" for d in deps]
            doc_str += f"\n\n{self.ICONS['dependency']} <b>{self.strings['v_reqs']}</b>\n<blockquote expandable>{chr(10).join(d_lines)}</blockquote>"
            
        return doc_str[:3900]

    def _build_kbd(self, item: dict, idx: int, group: list, search_phrase: str, is_expanded: bool = False) -> list:
        m_name = str(item.get("name", ""))
        kbd = [
            [
                {"text": self.strings["v_btn_copy"], "copy": search_phrase},
                {"text": self.strings["v_btn_dl"], "callback": self.cb_install, "args": (m_name, idx, group, search_phrase)},
                {"text": self.strings["v_btn_code"], "url": item.get("source_url")},
            ],
            [
                {"text": f"👍 {item.get('likes', 0)}", "callback": self.cb_rate, "args": (m_name, "like", idx, group, search_phrase)},
                {"text": f"👎 {item.get('dislikes', 0)}", "callback": self.cb_rate, "args": (m_name, "dislike", idx, group, search_phrase)},
            ]
        ]
        
        if group and len(group) > 1:
            prev_i = (idx - 1) % len(group)
            next_i = (idx + 1) % len(group)
            kbd.append([
                {"text": "◀️", "callback": self.cb_nav, "args": (prev_i, group, search_phrase)},
                {"text": self.strings["v_page"].format(idx=idx + 1, total=len(group)), "callback": self.cb_list, "args": (idx, group, search_phrase)},
                {"text": "▶️", "callback": self.cb_nav, "args": (next_i, group, search_phrase)},
            ])
            
        kbd.append([{
            "text": self.strings["v_btn_col" if is_expanded else "v_btn_exp"],
            "callback": self.cb_toggle,
            "args": (m_name, idx, group, search_phrase, not is_expanded)
        }])
        
        if is_expanded:
            kbd.append([
                {"text": self.strings["v_btn_talk"], "callback": self.cb_comments, "args": (m_name, idx, group, search_phrase)},
                {"text": self.strings["v_btn_sec"], "callback": self.cb_sec_check, "args": (m_name, idx, group, search_phrase)},
            ])
            
        return kbd


    async def _safe_edit(self, target: Any, text: str, kbd: list, img: Optional[str] = None) -> None:
        if hasattr(target, "inline_manager") and getattr(target, "inline_manager", None):
            try:
                imgr = target.inline_manager
                
                uid = getattr(target, "unit_id", None)
                if uid and hasattr(target, "_units") and uid in target._units:
                    target._units[uid]["buttons"] = kbd
                
                if img and img.startswith("http"):
                    await target.edit(text, reply_markup=kbd, photo=img)
                else:
                    await target.edit(text, reply_markup=kbd)
                return
            except Exception as e:
                log.warning("Bot API inline edit failed: %r", e)

        try:
            if hasattr(target, "edit"):
                await target.edit(text, reply_markup=kbd)
            else:
                await utils.answer(target, text, reply_markup=kbd)
                
        except TypeError:
            if hasattr(target, "edit"):
                await target.edit(text, reply_markup=kbd)
            else:
                await utils.answer(target, text, reply_markup=kbd)
                
        except Exception as e:
            log.warning("Fallback MTProto edit failed: %r", e)
            with suppress(Exception):
                await target.answer(self.strings["v_err_gui"], show_alert=True)



    @loader.command(
        ru_doc="<запрос> - поиск модулей в Vector.",
        jp_doc="<クエリ> - Vectorでモジュールを検索。",
        uk_doc="<запит> - пошук модулів у Vector.",
        de_doc="<Abfrage> - Suche nach Modulen in Vector.",
        neofit_doc="<query> - scout fer loot in Vector.",
        tiktok_doc="<запрос> - чекнуть темки (модули) в Vector.",
        leet_doc="<qu3ry> - 534rch m0dul35 1n V3c70r.",
        uwu_doc="<quewy> - seawch moduwes in Vectow (´• ω •`)."
    )
    async def vectorcmd(self, msg: Message):
        """<query> - search modules in Vector."""
        q = utils.get_args_raw(msg)
        if not q:
            return await utils.answer(msg, f"{self.ICONS['error']} <b>{self.strings['v_err_empty'].format(p=f'<code>{self.get_prefix()}')}</code></b>")
        if len(q) > 120:
            return await utils.answer(msg, f"{self.ICONS['warn']} <b>{self.strings['v_err_len']}</b>")

        form = await self.inline.form(
            f"{self.ICONS['search']} <b>{self.strings['v_loading_ui']}</b>",
            msg,
            reply_markup=[[{"text": "ㅤ", "callback": self.cb_dummy}]],
            photo="https://raw.githubusercontent.com/sepiol026-wq/GoyModules/refs/heads/main/assets/vsearch.png",
            silent=True
        )
        
        token = await self._get_active_token()
        log.info("Vector search request q=%r token=%s", q, bool(token))
        raw_res = await self._net_req("GET", "/api/search", token=token, params={"q": q, "limit": str(self.config["limit"])})
        if not token and self._last_ban_notice:
            return await self._safe_edit(form, self._last_ban_notice, [])
        
        if self._last_http_code == 401:
            log.info("Search got 401, retrying with forced token refresh")
            token = await self._get_active_token(force=True)
            raw_res = await self._net_req("GET", "/api/search", token=token, params={"q": q, "limit": str(self.config["limit"])})
            
        m_list = []
        if isinstance(raw_res, dict): m_list = raw_res.get("results", [])
        elif isinstance(raw_res, list): m_list = raw_res
        m_list = [self._normalize_module(x) for x in m_list if isinstance(x, dict)]
        
        if not m_list:
            return await self._safe_edit(form, f"{self.ICONS['error']} <b>{self.strings['v_err_404'].format(q=f'<code>{utils.escape_html(q)}</code>')}</b>", [])

        item = m_list[0]
        kbd = self._build_kbd(item, 0, m_list, q)
        text = self._build_html(item, 1, len(m_list))
        await self._safe_edit(form, text, kbd, item.get("banner"))

    @loader.command(
        ru_doc="Обновить модуль Vector.",
        jp_doc="Vectorモジュールを更新します。",
        uk_doc="Оновити модуль Vector.",
        de_doc="Vector-Modul aktualisieren.",
        neofit_doc="Upgrade the spyglass.",
        tiktok_doc="Обновить эту темку.",
        leet_doc="Upd473 V3c70r m0dul3.",
        uwu_doc="Update Vectow moduwe owo."
    )
    async def vecupdate(self, msg: Message):
        """Update Vector module from the registry."""
        args = utils.get_args_raw(msg)
        force = "-f" in args or "--force" in args

        m_name = "Vector"
        dl_path = f"/modules/{quote(m_name, safe='')}/source"
        dl_url = f"{API_ROOT}{dl_path}"

        if not force:
            token = await self._get_active_token()
            if not token:
                return await utils.answer(msg, self._last_ban_notice or f"{self.ICONS['error']} <b>{self.strings['v_err_api']}</b>")

            src_bytes = await self._net_req("GET", dl_path, token=token, as_bytes=True)
            if src_bytes:
                new_hash = hashlib.sha256(src_bytes).hexdigest()
                old_hash = self.get("vec_hash", "")
                if new_hash == old_hash:
                    await self.inline.form(
                        message=msg,
                        text=f"{self.ICONS['search']} <b>{self.strings['v_upd_req']}</b>\n\n{self.strings['v_upd_same']}",
                        reply_markup=[
                            [
                                {"text": self.strings["v_upd_force_btn"], "callback": self._vecupdate_force, "args": (src_bytes, new_hash), "style": "primary"},
                                {"text": self.strings["v_upd_cancel"], "action": "close", "style": "danger"},
                            ]
                        ],
                    )
                    return

        res, _ = await self._safe_install(m_name, dl_url, notify=False)
        if res == -1:
            return await utils.answer(msg, f"{self.ICONS['error']} <b>{self.strings['v_upd_err']}</b>")
        if res == 1:
            await utils.answer(msg, f"{self.ICONS['safe']} <b>{self.strings['v_upd_ok']}</b>")
        else:
            await utils.answer(msg, f"{self.ICONS['error']} <b>{self.strings['v_upd_err']}</b>")

    async def _vecupdate_force(self, call: Any, src_bytes: bytes, new_hash: str):
        with suppress(Exception):
            await call.answer()
        await call.edit(f"{self.ICONS['search']} <b>{self.strings['v_upd_req']}</b>")
        ldr = self.lookup("Loader")
        if not ldr or not hasattr(ldr, "load_module"):
            await call.answer(self.strings["v_upd_err"], show_alert=True)
            return
        doc = src_bytes.decode("utf-8")
        ok = await ldr.load_module(doc, call, name="Vector", origin="<vector-update>", save_fs=True)
        if ok:
            self.set("vec_hash", new_hash)
            await call.edit(f"{self.ICONS['safe']} <b>{self.strings['v_upd_ok']}</b>")
        else:
            await call.edit(f"{self.ICONS['error']} <b>{self.strings['v_upd_err']}</b>")

    @loader.watcher(chat_id=OFFICIAL_VECTOR_BOT_ID)
    async def vector_install_payload_watcher(self, msg: Message):
        text = (getattr(msg, "raw_text", None) or "").strip()
        if text == LANG_PING_PAYLOAD:
            with suppress(Exception):
                await self._client.send_message(msg.chat_id, f"{LANG_PONG_PREFIX}{self._detect_lang_suffix()}")
            with suppress(Exception):
                await msg.delete()
            return
        if not text.startswith("#v_payload:"):
            return

        with suppress(Exception):
            await msg.delete()

        parts = text.split(":", 4)
        if len(parts) != 5:
            return
        _, module_name, action, ts_raw, signature = parts
        if not module_name or not action or not ts_raw or not signature:
            return
        if action not in {"install", "like", "dislike"}:
            return
        if not re.fullmatch(r"[A-Za-z0-9._-]+", module_name):
            return
        if not ts_raw.isdigit():
            return

        ts = int(ts_raw)
        now = int(time.time())
        if abs(now - ts) > 60:
            return

        local_payload = f"{module_name}:{action}:{ts}"
        local_signature = hmac.new(
            AUTH_SALT.encode("utf-8"),
            local_payload.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        if not hmac.compare_digest(local_signature, signature):
            return

        async def send_feedback(status: str, reason: str = "", banned_until: str = "") -> None:
            feedback_ts = int(time.time())
            safe_reason = (reason or "").replace(":", " ").strip()
            safe_until = (banned_until or "").replace(":", " ").strip()
            feedback_payload = f"{module_name}:{action}:{status}:{feedback_ts}:{safe_reason}:{safe_until}"
            feedback_signature = hmac.new(
                AUTH_SALT.encode("utf-8"),
                feedback_payload.encode("utf-8"),
                hashlib.sha256,
            ).hexdigest()
            with suppress(Exception):
                await self._client.send_message(
                    msg.chat_id,
                    f"#v_feedback:{module_name}:{action}:{status}:{feedback_ts}:{safe_reason}:{safe_until}:{feedback_signature}",
                )

        token = await self._get_active_token()
        if not token:
            reason = "User is banned" if not self._last_ban_notice else self._last_ban_notice
            await send_feedback("banned", reason, "permanent")
            return

        if action == "install":
            dl_url = f"{API_ROOT}/modules/{quote(module_name, safe='')}/source"
            res, _ = await self._safe_install(module_name, dl_url, notify=False)
            if res == -1:
                await send_feedback("error")
            else:
                await send_feedback("ok" if res == 1 else "error")
            return

        uid = self._parse_jwt(token).get("sub", "")
        res = await self._net_req("POST", f"/api/rate/{quote(str(uid), safe='')}/{quote(module_name, safe='')}/{action}", token=token)
        if not res and self._last_http_code in {401, 403}:
            await send_feedback("banned", "User is banned", "permanent")
            return
        await send_feedback("ok" if res and res.get("ok") else "error")

    async def cb_dummy(self, cb: Any):
        with suppress(Exception): await cb.answer()

    async def cb_nav(self, cb: Any, target_i: int, group: list, q: str):
        with suppress(Exception): await cb.answer()
        if 0 <= target_i < len(group):
            item = group[target_i]
            await self._safe_edit(cb, self._build_html(item, target_i + 1, len(group)), self._build_kbd(item, target_i, group, q), item.get("banner"))

    async def cb_list(self, cb: Any, curr_i: int, group: list, q: str):
        with suppress(Exception): await cb.answer()
        kb = []
        for i in range(0, min(8, len(group))):
            m = group[i]
            kb.append([{"text": f"{i + 1}. {m.get('name')} by {m.get('author')}", "callback": self.cb_nav, "args": (i, group, q)}])
        if len(group) > 8:
            kb.append([{"text": "▶️", "callback": self.cb_page, "args": (1, group, q, curr_i)}])
        kb.append([{"text": "✖️", "callback": self.cb_nav, "args": (curr_i, group, q)}])
        await self._safe_edit(cb, f"{self.ICONS['modules_list']} <b>{self.strings['v_res_hdr']}</b>", kb)

    async def cb_page(self, cb: Any, pg: int, group: list, q: str, orig_i: int):
        with suppress(Exception): await cb.answer()
        kb = []
        start, end = pg * 8, min((pg + 1) * 8, len(group))
        for i in range(start, end):
            m = group[i]
            kb.append([{"text": f"{i + 1}. {m.get('name')} by {m.get('author')}", "callback": self.cb_nav, "args": (i, group, q)}])
        
        nav_row = []
        if pg > 0: nav_row.append({"text": "◀️", "callback": self.cb_page, "args": (pg - 1, group, q, orig_i)})
        if end < len(group): nav_row.append({"text": "▶️", "callback": self.cb_page, "args": (pg + 1, group, q, orig_i)})
        if nav_row: kb.append(nav_row)
        kb.append([{"text": "✖️", "callback": self.cb_nav, "args": (orig_i, group, q)}])
        await self._safe_edit(cb, f"{self.ICONS['modules_list']} <b>{self.strings['v_res_hdr']}</b>", kb)

    async def cb_toggle(self, cb: Any, m_name: str, i: int, group: list, q: str, exp: bool):
        with suppress(Exception): await cb.answer()
        item = group[i] if group and 0 <= i < len(group) else {"name": m_name, "source_url": f"{API_ROOT}/modules/{m_name}/source"}
        await self._safe_edit(cb, self._build_html(item, i + 1, len(group or [item])), self._build_kbd(item, i, group, q, exp), item.get("banner"))

    async def cb_rate(self, cb: Any, m_name: str, action: str, i: int, group: list, q: str):
        token = await self._get_active_token()
        if not token:
            with suppress(Exception): await cb.answer(self._last_ban_notice or self.strings["v_err_api"], show_alert=True)
            return
            
        uid = self._parse_jwt(token).get("sub", "")
        res = await self._net_req("POST", f"/api/rate/{quote(str(uid), safe='')}/{quote(m_name, safe='')}/{action}", token=token)
        if not res or not res.get("ok"):
            token = await self._get_active_token(force=True)
            uid = self._parse_jwt(token).get("sub", "")
            res = await self._net_req("POST", f"/api/rate/{quote(str(uid), safe='')}/{quote(m_name, safe='')}/{action}", token=token)
            if not res or not res.get("ok"):
                with suppress(Exception): await cb.answer(self.strings["v_dl_err"], show_alert=True)
                return

        new_likes, new_dislikes = self._extract_counts(res)
        if group and i < len(group):
            if new_likes is not None:
                group[i]["likes"] = new_likes
            if new_dislikes is not None:
                group[i]["dislikes"] = new_dislikes
            item = group[i]
        else:
            item = {"name": m_name, "likes": new_likes or 0, "dislikes": new_dislikes or 0, "source_url": f"{API_ROOT}/modules/{m_name}/source"}
            
        await self._safe_edit(cb, self._build_html(item, i + 1, len(group or [item])), self._build_kbd(item, i, group, q), item.get("banner"))
        s_val = res.get("rating", {}).get("state")
        with suppress(Exception): await cb.answer(self.strings["v_fb_rm" if s_val == "removed" else "v_fb_add"], show_alert=True)

    async def cb_install(self, cb: Any, m_name: str, i: int, group: list, q: str):
        token = await self._get_active_token()
        if not token:
            with suppress(Exception): await cb.answer(self._last_ban_notice or self.strings["v_err_api"], show_alert=True)
            return

        dl_url = f"{API_ROOT}/modules/{quote(m_name, safe='')}/source"
        res, errors = await self._safe_install(m_name, dl_url)
        if res == -1:
            with suppress(Exception): await cb.answer(self.strings["v_dl_err"], show_alert=True)
            return
        if res == 1:
            with suppress(Exception): await cb.answer(self.strings["v_dl_ok"], show_alert=True)
            return

        if errors:
            item = group[i] if group and 0 <= i < len(group) else {"name": m_name, "source_url": dl_url}
            err_text = self._fmt_install_errors(m_name, errors)
            await self._safe_edit(cb, err_text, self._build_kbd(item, i, group, q), item.get("banner"))
        else:
            with suppress(Exception): await cb.answer(self.strings["v_dl_err"], show_alert=True)

    async def cb_sec_check(self, cb: Any, m_name: str, i: int, group: list, q: str):
        def _get_sec_kb(has_run: bool):
            k = [[
                {"text": self.strings["v_btn_bck"], "callback": self.cb_nav, "args": (i, group or [], q)},
                {"text": self.strings["v_btn_code"], "url": f"{API_ROOT}/modules/{m_name}/source"},
            ]]
            if not has_run: k.append([{"text": self.strings["v_btn_aud_run"], "callback": self.cb_sec_run, "args": (m_name, i, group, q)}])
            return k

        cached = self._security_cache.get(m_name)
        if cached and cached.get("check"):
            return await self._safe_edit(cb, f"{self.ICONS['safe']} <i>{self.strings['v_aud_mem']}</i>\n\n{self._fmt_sec(m_name, cached)}", _get_sec_kb(True))

        await self._safe_edit(cb, f"{self.ICONS['search']} <b>{self.strings['v_aud_req']}</b>", _get_sec_kb(True))
        token = await self._get_active_token()
        if not token:
            with suppress(Exception): await cb.answer(self._last_ban_notice or self.strings["v_err_api"], show_alert=True)
            return
        res = await self._net_req("GET", f"/api/modules/{quote(m_name, safe='')}/security-check", token=token)
        
        if not res or self._last_http_code >= 400:
            return await self._safe_edit(cb, f"{self.ICONS['error']} <b>{self.strings['v_aud_err']}</b>", _get_sec_kb(True))

        if res.get("check"): self._security_cache[m_name] = res
        await self._safe_edit(cb, self._fmt_sec(m_name, res), _get_sec_kb(bool(res.get("checked"))))

    async def cb_sec_run(self, cb: Any, m_name: str, i: int, group: list, q: str):
        await self._safe_edit(cb, f"{self.ICONS['search']} <b>{self.strings['v_aud_proc']}</b>", [[{"text": self.strings["v_btn_bck"], "callback": self.cb_nav, "args": (i, group or [], q)}]])
        token = await self._get_active_token()
        if not token:
            with suppress(Exception): await cb.answer(self._last_ban_notice or self.strings["v_err_api"], show_alert=True)
            return
        res = await self._net_req("POST", f"/api/modules/{quote(m_name, safe='')}/security-check", token=token, timeout=120)
        
        if self._last_http_code == 429:
            return await self._safe_edit(cb, f"{self.ICONS['warn']} <b>{self.strings['v_aud_zero']}</b>", [[{"text": self.strings["v_btn_bck"], "callback": self.cb_nav, "args": (i, group or [], q)}]])
        if not res or self._last_http_code >= 400:
            return await self._safe_edit(cb, f"{self.ICONS['error']} <b>{self.strings['v_aud_err']}</b>", [[{"text": self.strings["v_btn_bck"], "callback": self.cb_nav, "args": (i, group or [], q)}]])

        if res.get("check"): self._security_cache[m_name] = res
        await self._safe_edit(cb, self._fmt_sec(m_name, res), [[
            {"text": self.strings["v_btn_bck"], "callback": self.cb_nav, "args": (i, group or [], q)},
            {"text": self.strings["v_btn_code"], "url": f"{API_ROOT}/modules/{m_name}/source"},
        ]])

    def _fmt_sec(self, m_name: str, payload: dict) -> str:
        chk = payload.get("check")
        qta = payload.get("quota") or (chk.get("quota") if chk else None) or {}
        if not chk:
            return (f"{self.ICONS['shield']} <b>{self.strings['v_aud_hdr'].format(name=m_name)}</b>\n\n"
                    f"{self.ICONS['warn']} {self.strings['v_aud_none']}\n"
                    f"{self.ICONS['quota']} <i>{self.strings['v_aud_left'].format(remaining=qta.get('remaining', '?'), limit=qta.get('limit', '?'))}</i>")

        v = str(chk.get("verdict", "unknown"))
        v_icon = self.ICONS.get(v, self.ICONS['shield'])
        static = chk.get("details", {}).get("static", {})
        fnds = static.get("findings", {})
        
        lines = [
            f"{v_icon} <b>{self.strings['v_aud_hdr'].format(name=m_name)}</b>\n",
            f"{self.ICONS['shield']} <b>{self.strings['v_aud_lvl']}:</b> <code>{chk.get('label', v)}</code> (<code>{chk.get('confidence', 0)}%</code>)",
            f"{self.ICONS['stats']} <b>{self.strings['v_aud_stat']}:</b> risk <code>{static.get('risk', 'unknown')}</code>, score <code>{static.get('score', '?')}</code>",
            f"{self.ICONS['description']} <b>{self.strings['v_aud_out']}:</b>\n<blockquote expandable>{chk.get('summary', self.strings['v_aud_no_txt'])}</blockquote>"
        ]
        
        f_blocks = []
        for hdr, key in [(self.strings["v_sig_crit"], "critical"), (self.strings["v_sig_warn"], "warning"), (self.strings["v_sig_info"], "info")]:
            arr = fnds.get(key, [])
            if arr: f_blocks.append(f"<b>{hdr}</b>: " + ", ".join(x.get("title", "?") for x in arr[:3]))
        if f_blocks:
            lines.append(f"{self.ICONS['search']} <b>{self.strings['v_aud_sigs']}:</b>\n<blockquote expandable>{chr(10).join(f_blocks)}</blockquote>")
            
        lines.append(f"{self.ICONS['quota']} <i>{self.strings['v_aud_left'].format(remaining=qta.get('remaining', '?'), limit=qta.get('limit', '?'))}</i>")
        return "\n".join(lines)

    async def cb_comments(self, cb: Any, m_name: str, i: int, group: list, q: str):
        with suppress(Exception): await cb.answer()
        token = await self._get_active_token()
        if not token:
            with suppress(Exception): await cb.answer(self._last_ban_notice or self.strings["v_err_api"], show_alert=True)
            return
        res = await self._net_req("GET", f"/api/modules/{quote(m_name, safe='')}/comments", token=token)
        
        if not res or not isinstance(res, dict):
            with suppress(Exception): await cb.answer(self.strings["v_talk_err"], show_alert=True)
            return
            
        kb = [[
            {"text": self.strings["v_btn_bck"], "callback": self.cb_nav, "args": (i, group or [], q)},
            {"text": self.strings["v_btn_wrt"], "input": self.strings["v_rep_ask"], "handler": self.cb_post_comment, "args": (m_name, i, group, q)},
            {"text": self.strings["v_btn_site"], "url": f"{API_ROOT}/modules/{m_name}/source"},
        ]]
        
        item = group[i] if group and 0 <= i < len(group) else {}
        await self._safe_edit(cb, self._fmt_comments(res.get("comments", []), m_name), kb, item.get("banner"))

    async def cb_post_comment(self, cb: Any, text: str, m_name: str, i: int, group: list, q: str):
        token = await self._get_active_token()
        if not token:
            with suppress(Exception): await cb.answer(self._last_ban_notice or self.strings["v_err_api"], show_alert=True)
            return
        c_txt = str(text or "").strip()
        if not c_txt:
            with suppress(Exception): await cb.answer(self.strings["v_rep_cncl"], show_alert=True)
            return
        if len(c_txt) < 2 or len(c_txt) > 1800:
            with suppress(Exception): await cb.answer(self.strings["v_rep_min" if len(c_txt) < 2 else "v_rep_max"], show_alert=True)
            return

        with suppress(Exception): await cb.answer(self.strings["v_rep_snt"], show_alert=True)
        res = await self._net_req("POST", f"/api/modules/{quote(m_name, safe='')}/comments", token=token, json_data={"body": c_txt})
        
        if not res:
            with suppress(Exception): await cb.answer(self.strings["v_rep_err"], show_alert=True)
            return
            
        with suppress(Exception): await cb.answer(self.strings["v_rep_ok"], show_alert=True)
        
        await asyncio.sleep(1.5)
        
        await self.cb_comments(cb, m_name, i, group, q)

    def _fmt_comments(self, comments: list, m_name: str) -> str:
        h = f"{self.strings['v_talk_hdr'].format(emoji=self.ICONS['comments'], name=m_name)}\n<b>{self.strings['v_talk_desc']}</b>\n<i>{self.strings['v_talk_num'].format(count=len(comments))}</i>"
        if not comments: return f"{h}\n\n{self.strings['v_talk_0']}"
        
        roots, chmap = [], {}
        for c in comments:
            pid = c.get("parent_id")
            if pid: chmap.setdefault(str(pid), []).append(c)
            else: roots.append(c)
            if c.get("replies"): chmap.setdefault(str(c.get("id")), []).extend(c["replies"])

        blks = [h]
        for r in roots[:10]:
            rid = str(r.get("id"))
            
            uname = str(r.get("author_username", "")).strip().lstrip("@")
            meta = [f"@{utils.escape_html(uname)}"] if uname else []
            ts = str(r.get("created_at", "")).replace("T", " ").replace("Z", "").strip()
            if ts: meta.append(utils.escape_html(ts[:16]))
            meta_str = f" <i>{' · '.join(meta)}</i>" if meta else ""
            edit_mark = " *" if r.get("can_edit") else ""
            
            auth = f"<b>{utils.escape_html(r.get('author_name') or r.get('author_username') or 'Unknown')}</b>{edit_mark}{meta_str}"
            blks.append(f"╭─ {auth}\n╰─\n<blockquote>{utils.escape_html(r.get('body', ''))}</blockquote>")
            
            subs = chmap.get(rid, [])
            for s in subs[:4]:
                s_uname = str(s.get("author_username", "")).strip().lstrip("@")
                s_meta = [f"@{utils.escape_html(s_uname)}"] if s_uname else []
                s_ts = str(s.get("created_at", "")).replace("T", " ").replace("Z", "").strip()
                if s_ts: s_meta.append(utils.escape_html(s_ts[:16]))
                s_meta_str = f" <i>{' · '.join(s_meta)}</i>" if s_meta else ""
                s_edit_mark = " *" if s.get("can_edit") else ""
                
                s_auth = f"<b>{utils.escape_html(s.get('author_name') or s.get('author_username') or 'Unknown')}</b>{s_edit_mark}{s_meta_str}"
                blks.append(f"  {self.ICONS['reply']} {s_auth}\n<blockquote>{utils.escape_html(s.get('body', ''))}</blockquote>")
                
            if len(subs) > 4: blks.append(f"  <i>{self.strings['v_more_replies'].format(count=len(subs)-4)}</i>")
            
        if len(comments) > sum(1 + len(chmap.get(str(r.get("id")), [])[:4]) for r in roots[:10]):
            blks.append(f"<i>{self.strings['v_more_comments']}</i>")
            
        return "\n\n".join(blks)