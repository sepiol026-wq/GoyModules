# GoyPulse V9

Module for Heroku UserBot.

## Features

- auto-replies in groups;
- training on chat history;
- context-aware responses;
- separate memory per chat;
- user ignore list;
- temporary mute mode;
- chat activity and tone analysis;
- text replies and media replies;
- backups and restore;
- backup sharing between users;
- trust/keycard exchange for backup transfer;
- update checks and update application;
- hidden mode for internal module commands.

## Installation

1. Download `goypulse.py` from the repository.
2. Send the file to any Telegram chat.
3. Reply to the file with:

```text
.lm
```

4. The Heroku UserBot will install the module automatically.

## Usage

### Enable the module

```text
.gpulse on
```

### Disable the module

```text
.gpulse off
```

### Train on chat history

```text
.gpref
```

### Check status

```text
.gpstat
```

### Inspect chat behavior

```text
.gpinfo
```

### Temporarily mute replies

```text
.gpmute <minutes>
```

### Reset or clear memory

```text
.gpclear
.gpreset
```

### Stop the module globally

```text
.gpkill
```

## Commands

### Main commands

- `.gpulse on` — enable in the current chat
- `.gpulse off` — disable in the current chat
- `.gpref` — train on chat history
- `.gpstat` — show status and settings
- `.gpinfo` — show chat analysis
- `.gpmute <minutes>` — mute replies for a limited time
- `.gpreset` — reset the current chat completely
- `.gpclear` — clear current chat memory
- `.gpkill` — stop the module globally

### Ignore

- `.gpignore` — add or remove a user from ignore by replying to their message

### Settings

```text
.gpset <parameter> <value>
.gpset <parameter> <value> <chat_id>
```

Available parameters:

- `lim` — history limit;
- `min` — minimum number of messages before the module starts working;
- `ch` — chance of a normal reply;
- `mch` — chance of a media reply;
- `mych` — chance of a reply to a reply;
- `cdm` — minimum delay;
- `cdx` — maximum delay;
- `bpon` — auto-backup;
- `bpint` — auto-backup interval;
- `react` — reaction chance;
- `logerr` — log errors;
- `logstl` — log hidden mode activity;
- `logbkp` — log backups;
- `loglrn` — log training;
- `logans` — log bot replies.

### Backups

- `.gpbackup status` — show backup status
- `.gpbackup here` — back up the current chat
- `.gpbackup all` — back up all chats
- `.gpbackup <chat1> [chat2 ...]` — back up selected chats
- `.gpbackup share <user> <targets...>` — share backup with another user
- `.gpbackup trust <user|reply>` — exchange trust keys

### Restore

- `.gprestore` — restore from a replied backup file or text
- `.gprestore --force` — restore without extra confirmation

### Updates

- `.gpupdate check` — check for updates
- `.gpupdate apply` — apply the update
- `.gpupdate status` — show update status

### Hidden mode

- `.gph <target> <command>` — run an allowed GoyPulse command in another chat

Allowed commands for hidden mode:

- `gpstat`
- `gpinfo`
- `gpulse`
- `gpset`
- `gpmute`
- `gpignore`
- `gpref`
- `gpupdate`

## Backup Flow

### Standard flow

1. Create a backup of the current chat or selected chats.
2. Share it with a trusted user if needed.
3. Restore it on another account or after reinstalling the module.
4. Recheck settings and training state after restore.

### Common backup scenarios

#### 1. Share your setup with a friend
Create a backup, exchange trust with `.gpbackup trust <user>`, then send the backup with `.gpbackup share <user> <targets...>`.

#### 2. Move memory to a new account
Back up the chats on the old account, install the module on the new account, then restore the backup there.

#### 3. Save everything before a reset
Before using `.gpreset` or clearing memory, create a backup so the current state can be restored later.

#### 4. Keep a snapshot before changing settings
If you plan to change chance, delay, or history parameters, back up first and restore if the new configuration is worse.

#### 5. Preserve a specific chat only
Use `.gpbackup here` or `.gpbackup <chat1>` when you only need one chat, not the full dataset.

#### 6. Export multiple chats at once
Use `.gpbackup <chat1> [chat2 ...]` when you want to move several chats together.

#### 7. Duplicate your setup on another account
Create a backup once, then restore it on a second account to reproduce the same chat behavior.

#### 8. Transfer a curated memory set
Back up only the chats that matter, then share them with someone who needs a specific part of your memory set.

#### 9. Prepare for accidental wipe protection
Keep a backup before reinstallation, device changes, or module replacement.

#### 10. Restore after a bad training run
If training produced weak or noisy behavior, restore a backup from before the bad data was added.

#### 11. Send a ready-made configuration to a teammate
If someone needs the same tuning, share the backup and let them restore it on their own account.

#### 12. Keep a clean archive of an older chat state
Store an older snapshot before a big change in chat tone, community members, or response settings.

## Examples

### Basic setup

```text
.gpulse on
.gpref
.gpset ch 45
.gpset cdm 4
.gpset cdx 12
```

### Back up and share

```text
.gpbackup here
.gpbackup trust @friend
.gpbackup share @friend -1001234567890
```

### Restore

```text
.gprestore
```

Reply to the backup file or backup text, then run the command.

## Notes

- each chat has its own memory and settings;
- response quality depends on the amount and quality of the history;
- with very little data, behavior will be weaker;
- media replies depend on what is already in memory;
- backups may use encryption if `cryptography` is available;
- update issues may trigger a limited recovery mode.

## Version

`V9`

Author: [`goy`](https://t.me/samsepi0l_ovf)
