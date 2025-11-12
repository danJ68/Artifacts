# Peace Corps Social Entrepreneurship Simulation Game

An interactive, turn-based educational simulation that helps high school students explore what it's like to be a Peace Corps Volunteer working on sustainable development projects.

## Overview

This simulation guides students through a realistic role-playing scenario where they:
- Choose from three different international development contexts
- Build relationships with community members
- Navigate cultural dynamics and power structures
- Design sustainable development projects
- Receive feedback on their approach

## Features

- **Three Unique Scenarios:**
  - Agricultural Development in Rural Ghana
  - Youth Education & Empowerment in Urban Peru
  - Clean Water & Environmental Health in Coastal Philippines

- **Realistic Role-Play:** Interact with AI-powered community members who respond based on your approach

- **Intelligent Feedback System:** Tracks your decisions and provides personalized feedback on:
  - Active listening skills
  - Sustainability thinking
  - Cultural sensitivity
  - Asset-based community development

- **Save/Load Functionality:** Your progress is automatically saved, so you can continue later

- **Educational Focus:** Aligned with UN Sustainable Development Goals and Peace Corps best practices

## Requirements

- Python 3.6 or higher
- No additional libraries required (uses only Python standard library)

## How to Run

1. Make sure you have Python 3 installed:
   ```bash
   python3 --version
   ```

2. Make the game executable (optional):
   ```bash
   chmod +x peace_corps_game.py
   ```

3. Run the game:
   ```bash
   python3 peace_corps_game.py
   ```

   Or if you made it executable:
   ```bash
   ./peace_corps_game.py
   ```

## How to Play

### Phase 1: Introduction
Share your background knowledge about international development, social entrepreneurship, or the Peace Corps.

### Phase 2: Scenario Selection
Choose one of three scenarios based on your interests:
- Type `1` for Ghana (Agricultural Development)
- Type `2` for Peru (Youth Education)
- Type `3` for Philippines (Clean Water & Sanitation)

### Phase 3: Scenario Details
Read carefully about your role, the community, and cultural context.

### Phase 4: Role-Play
Engage with community members through text-based conversation:
- **Listen first:** Ask questions before proposing solutions
- **Think sustainably:** Consider what happens after you leave
- **Respect culture:** Be aware of local customs and power dynamics
- **Build on strengths:** Look for existing community assets

### Phase 5: Decision Point
Make a critical choice about how to move forward with your project.

### Phase 6: Feedback
Receive personalized feedback on your approach, with specific examples from your choices.

## Tips for Success

1. **Don't rush to solutions** - Real Peace Corps volunteers spend months just listening and building relationships

2. **Ask about sustainability** - The best projects continue after the volunteer leaves

3. **Look for community assets** - Every community has existing knowledge, skills, and resources

4. **Be culturally humble** - Understand that change must come from within the community

5. **Think long-term** - Build relationships and systems, not dependencies

## Game Features

- **Auto-save:** Your game is automatically saved after each phase
- **Continue game:** When you restart, you'll be asked if you want to continue from where you left off
- **Multiple playthroughs:** Try different scenarios and approaches to deepen your understanding

## Educational Value

This simulation teaches:
- **Sustainable development principles**
- **Cross-cultural communication**
- **Community-based development approaches**
- **Systems thinking**
- **Cultural humility**
- **Asset-based community development (ABCD)**

## Learning Outcomes

Students will:
- Understand the difference between charity and sustainable development
- Practice active listening and needs assessment
- Recognize the importance of cultural context in development work
- Learn to build on existing community strengths
- Experience the complexity of real-world development challenges

## About Peace Corps

The Peace Corps is a U.S. government program that sends American volunteers to work on development projects in communities around the world. Volunteers serve for 27 months (3 months training + 24 months service) in sectors including:
- Education
- Health
- Agriculture
- Environment
- Youth Development
- Community Economic Development

Learn more at: [www.peacecorps.gov](https://www.peacecorps.gov)

## Technical Details

- **Save file:** `save_game.json` (created in the same directory as the game)
- **Game state:** Tracks all conversation history and player decisions
- **Response analysis:** Uses keyword matching to understand player intent
- **Feedback tracking:** Monitors 8 different behavioral indicators

## Troubleshooting

**Game won't start:**
- Check that you have Python 3.6 or higher
- Make sure you're running it with `python3` not `python`

**Want to start fresh:**
- Delete `save_game.json` file
- Or answer "no" when asked if you want to continue

**Save file corrupted:**
- Delete `save_game.json` and start a new game

## Credits

Based on the Peace Corps Social Entrepreneurship Simulation prompt designed for educational purposes.

## License

This educational simulation is provided for learning purposes.
