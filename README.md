# ScamShield AI

## Project Overview

ScamShield AI is an AI-powered assistant designed to help users examine suspicious emails, text messages, and online messages. It highlights potential warning signs, estimates the level of risk, and recommends practical steps the user can take to protect themselves.

The project addresses the difficulty many people face when trying to determine whether an unfamiliar or urgent message can be trusted.

## Current State and Project Goal

ScamShield AI is currently in the early stages of development. The first version will be a Python command-line application that accepts a suspicious message and returns a structured risk analysis using the OpenAI API.

The long-term goal is to develop it into a more complete digital-safety assistant capable of examining different types of content, explaining common scam techniques, supporting follow-up questions, and providing accessible safety guidance through a user-friendly interface.

## Features

The initial version is intended to allow users to:

- Submit suspicious emails, SMS messages, or online messages for analysis.
- Receive a risk assessment such as low, medium, or high risk.
- Identify suspicious wording, urgency tactics, unusual requests, and other warning signs.
- Understand what information, payment, or action the sender is requesting.
- Receive practical recommendations for verifying the message safely.
- Ask follow-up questions about the analysis.
- Get results in a clear and consistent format.

> ScamShield AI provides guidance based on patterns found in the submitted content. It cannot guarantee that a message is safe or confirm with certainty that it is a scam.

## Tech Stack

- **Python:** Used to build the application, collect user input, manage the program flow, and display the analysis.
- **OpenAI API:** Used to analyze submitted messages and generate structured, understandable safety guidance.
- **Prompt engineering:** Used to define the assistant’s role, separate untrusted message content from instructions, and produce consistent results.
- **python-dotenv:** Used to load the OpenAI API key from a local environment file without placing the key directly in the source code.
- **Git and GitHub:** Used for version control, documenting progress, and managing the project as it develops.
- **Visual Studio Code:** Used as the primary development environment.

## Project Structure

_To be added as the project structure develops._

## Installation and Setup

_To be added after the initial application has been implemented._

## Usage

The planned usage flow for the first version is:

1. Start the application from the terminal.
2. Paste or enter the suspicious message.
3. Submit the message for analysis.
4. Review the generated risk level, warning signs, explanation, and recommended next steps.
5. Ask a follow-up question or analyze another message.

Users should remove passwords, banking details, identification numbers, and other sensitive personal information before submitting a message.

## API Documentation

_To be added when the application’s API usage has been implemented._

## Testing

_To be added when the first test cases have been created._

## Limitations and Future Improvements

### Current Limitations

- The application cannot guarantee whether a message is legitimate or fraudulent.
- Its assessment depends on the information contained in the submitted message.
- It does not independently verify senders, phone numbers, websites, or organizations.
- It may miss sophisticated scams or incorrectly flag legitimate messages.
- The first version will only accept text input.
- The quality of the results depends on the prompts and model responses.
- Users must avoid submitting sensitive personal or financial information.

### Future Improvements

- Add support for suspicious URLs and domain analysis.
- Allow users to upload screenshots of suspicious messages.
- Support multiple languages.
- Add email-header analysis.
- Introduce more detailed scam categories and explanations.
- Provide educational examples of common scam techniques.
- Build a web-based user interface.
- Add automated tests and prompt evaluation cases.
- Improve privacy controls and handling of submitted content.
- Include links to appropriate reporting and support services based on the user’s location.
