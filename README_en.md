# GoyPulse V9 🧠

[Russian Version](README_ru.md)

## Description
GoyPulse is an advanced Markov-chain based module for Telegram userbots (like Friendly-Telegram). It allows the bot to learn from chat history and mimic human-like interaction while maintaining context and style.

## Key Features
*   **Training**: Message collection and analysis for linguistic model building.
*   **Auto-responder**: Intelligent response generation based on recent context.
*   **Stealth Mode (.gph)**: Command execution in other chats without user visibility (results in log channel).
*   **Security**:
    *   **GPB2 Backup**: Database backup encryption using Ed25519 (X25519) and AEAD.
    *   **Update Verification**: All official updates are signed with a digital signature.
    *   **Self-Integrity Check**: Protection against unauthorized code tampering.
*   **Logging**: Dedicated channel for system events, errors, and reports.

## Installation
Send this command in any chat:
`.dlm https://raw.githubusercontent.com/sepiol026-wq/goypulse/main/goypulse.py`

## Commands
*   `.gpulse [on/off]` — Enable/disable the bot in a chat.
*   `.gpref` — Start training in the current chat.
*   `.gpstat` — Database and chat statistics.
*   `.gpinfo` — Chat "vibe" analysis and user activity.
*   `.gpupdate` — Check and apply updates.
*   `.gpbackup` — Backup management (encryption, export).

---
*Developed for personal use. Respect chat rules and communication ethics.*
*Author: @samsepi0l_ovf*
