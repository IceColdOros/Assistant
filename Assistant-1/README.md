AI Assistant Application
Overview

This project is a desktop AI assistant that can be instantly activated via a custom hotkey. The assistant supports both text and voice interactions, and can be paired with external devices (e.g., Alexa) for enhanced functionality.

The application aims to provide an unobtrusive, fast-access interface for AI queries while maintaining a clean and minimal design.

Features
1. Hotkey Activation

Launch the AI assistant instantly by pressing a predefined hotkey.
Interface appears as a popup menu, similar to the Windows Start menu.

2. Text and Voice Modes

Type a query directly into the text box.
Use the voice toggle to speak a query.
Responses match the input mode (voice → voice reply with transcript, text → text reply with optional voice output).

3. UI and Interaction

Minimalistic dark UI (semi-transparent background, blur effect for focus).
Text input box with a voice icon for mode switching.
Voice-only mode displays a small floating icon while maintaining background conversation recording.

4. Persistent Conversations

Conversations are stored locally for reference.
Future goal: build AI personality traits over time based on past interactions.

5. Extended Capabilities

Google-style assistant features, e.g.:
Show locations in Google Earth.
Play and control media (Spotify, YouTube, etc.).
Perform research or coding assistance.
Modular design for integration with third-party APIs and services.

6. Application-Specific Volume Control (Future Feature)

Map specific running applications to dedicated hardware controls (e.g., keyboard wheel).
Adjust only the selected application’s volume without affecting system-wide audio.
Ideal for scenarios like lowering game music while maintaining voice chat volume.

Target Objectives

Popup menu triggered by a custom hotkey.
Non-intrusive operation — accessible anytime without disrupting workflow.
Dual input modes: text and voice.
Customizable integrations for maps, media, research tools, and other software.

Future Plans

Raspberry Pi hosting for independent operation.
Alexa or other smart assistant integration.
Personality-building AI that adapts to user habits and preferences.