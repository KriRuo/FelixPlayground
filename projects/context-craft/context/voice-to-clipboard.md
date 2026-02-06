---
id: voice-to-clipboard
name: Voice to Clipboard
status: active
updated: 2026-02-06
owner: Kris
---

# Voice to Clipboard

## Vision
A local, private tool that lets Kris speak and have words instantly appear wherever the cursor is. No cloud, no latency, no privacy concerns.

**Success looks like:** Press hotkey → speak → text appears at cursor. Under 3 seconds total.

## Users
- **Primary:** Kris (power user, developer, types a lot)
- **Context:** Working in WSL2 on Windows, needs system-wide input

## Pain Points
1. **Typing is slower than thinking** — speaking is 3-4x faster
2. **Cloud transcription = privacy risk** — existing tools send audio to servers
3. **Context switching kills flow** — opening a separate app breaks focus
4. **Existing solutions are bloated** — want something minimal and fast

## Requirements

### Must Have
- [ ] Press hotkey → microphone activates
- [ ] Visual indicator that mic is listening
- [ ] Speak → transcribed locally via faster_whisper
- [ ] Release hotkey → text pasted at cursor position
- [ ] Works system-wide (any application)
- [ ] Runs 100% local (zero network calls)

### Should Have
- [ ] Configurable hotkey
- [ ] Language selection
- [ ] Adjustable model size (speed vs accuracy tradeoff)
- [ ] Tray icon / minimal UI

### Won't Have (v1)
- Cloud transcription option
- Mobile app
- Voice commands (this is transcription, not assistant)
- Punctuation/formatting AI
- Multi-speaker detection

## Constraints
- **Language:** Python
- **Transcription:** faster_whisper (local Whisper implementation)
- **Platform:** Windows + WSL2 (KrisLaptop)
- **Performance:** < 2 seconds transcription for 10s of speech
- **Privacy:** Zero network calls during operation

## Technical Challenges
1. **WSL2 ↔ Windows audio:** How to capture mic from Windows in WSL2?
   - Option A: Run Python natively on Windows
   - Option B: PulseAudio bridge to WSL2
   - Option C: Windows service + WSL2 processing
2. **Global hotkey:** Capture hotkey system-wide from WSL2?
   - May need Windows-side component
3. **Clipboard paste:** How to paste at cursor cross-platform?

## User Journey
```
1. Kris is writing an email in Outlook
2. Has a thought, doesn't want to type it
3. Holds down Ctrl+Shift+Space (configurable)
4. Sees small indicator: "🎤 Listening..."
5. Speaks: "Let's schedule a call for next Tuesday afternoon"
6. Releases hotkey
7. Indicator shows: "⏳ Transcribing..."
8. Text appears at cursor in Outlook
9. Kris continues working — total time < 3 seconds
```

## Non-Goals
- This is NOT a voice assistant (no commands, no AI responses)
- This is NOT a dictation app (no formatting, no punctuation AI)
- This is NOT a meeting transcriber (single-shot input only)
- This is NOT cross-platform (Windows/WSL2 only for v1)

## Notes
- Kris has already started working on this
- Uses faster_whisper library
- Repo exists on GitHub (not yet shared with Felixx)
