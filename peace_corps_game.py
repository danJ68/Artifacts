#!/usr/bin/env python3
"""
Peace Corps Social Entrepreneurship Simulation Game
A turn-based educational simulation for high school students
"""

import json
import os
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class GamePhase(Enum):
    """Game phases"""
    INTRO = "intro"
    SCENARIO_SELECTION = "scenario_selection"
    SCENARIO_DETAILS = "scenario_details"
    ROLE_PLAY = "role_play"
    DECISION_POINT = "decision_point"
    FEEDBACK = "feedback"
    COMPLETE = "complete"


@dataclass
class PlayerProfile:
    """Stores player background information"""
    background_knowledge: str = ""
    interests: str = ""
    chosen_scenario: Optional[str] = None


@dataclass
class GameState:
    """Manages the current state of the game"""
    phase: GamePhase = GamePhase.INTRO
    player: PlayerProfile = field(default_factory=PlayerProfile)
    turn_count: int = 0
    conversation_history: List[Dict[str, str]] = field(default_factory=list)
    player_actions: List[str] = field(default_factory=list)

    # Tracking for feedback
    showed_listening: bool = False
    asked_about_assets: bool = False
    considered_sustainability: bool = False
    showed_cultural_sensitivity: bool = False
    jumped_to_solutions: bool = False
    missed_sustainability: bool = False
    overlooked_culture: bool = False
    ignored_existing_strengths: bool = False


class ScenarioData:
    """Contains all scenario information"""

    SCENARIOS = {
        "ghana": {
            "name": "Agricultural Development in Rural Ghana",
            "description": "You're assigned to a small farming village that's been struggling with food security. The community grows cocoa for export but has difficulty growing enough food for themselves. You'll work with local farmers, women's groups, and the village chief to explore sustainable solutions.",
            "details": {
                "time_in_community": "3 months",
                "key_people": [
                    "Chief Kofi - The village chief, a respected elder in his 60s who is cautious about outsiders but cares deeply about his community",
                    "Ama - Leader of the women's farming cooperative, innovative and outspoken about food security issues",
                    "Kwame - A young farmer in his 30s who has some secondary education and is interested in new farming techniques"
                ],
                "observations": "The village has rich soil and strong community bonds. Cocoa prices have been volatile, causing economic stress. Women do most of the food farming but have less access to land and resources. There's existing knowledge of traditional crops that has been somewhat forgotten in favor of cash crops.",
                "living_situation": "You live in a small compound with a local family, sharing meals and learning Twi language basics.",
                "sdg": "SDG 2: Zero Hunger - End hunger, achieve food security and improved nutrition, and promote sustainable agriculture",
                "cultural_considerations": [
                    "Decision-making traditionally flows through the chief and council of elders. Going around this structure can create problems.",
                    "Gender roles are significant - men control most land decisions, but women do much of the farming work."
                ]
            },
            "role_play": {
                "opening_scene": """
**BEGIN ROLE-PLAY**

You're sitting under the large mango tree in the village center where community meetings are held. It's early evening, and about 20 community members have gathered. Chief Kofi sits in his chair at the front, and you're seated to the side as an honored guest.

Ama, the women's cooperative leader, stands up to speak, her voice firm:

"Chief, with respect, we must talk about the hungry season. Every year between harvests, our children's bellies are empty. We grow cocoa to sell, yes, but we cannot eat cocoa. My women, we try to grow cassava and plantain between the cocoa trees, but the land is not enough and belongs to our husbands' families."

Chief Kofi nods slowly. "This is true. The cocoa brings money, but not always enough, and not always when we need it." He turns to look at you. "You are the Peace Corps volunteer. You have come from America where there is much food. What do you think we should do?"

The crowd turns to look at you expectantly. You notice Kwame, the young farmer, leaning forward with interest, while some of the older men look more skeptical.

What do you say or do?
""",
                "responses": {
                    "listening": {
                        "keywords": ["question", "ask", "learn", "tell me", "understand", "experience", "thoughts", "ideas", "challenges", "tried"],
                        "reaction": """
Ama's expression softens slightly. "You want to know what we have tried? Many things, but the problems remain. The agricultural officer from the district came once and told us to use fertilizer we cannot afford. An NGO gave us seeds for vegetables five years ago, but they needed too much water and we have only rain. Now those seeds are gone."

Chief Kofi adds, "We are not helpless people. Our grandparents grew many crops - different yams, millet, vegetables. But the government encouraged cocoa for the economy. Now young people only know cocoa."

Kwame speaks up: "I have heard of farmer field schools, where people learn together. And some villages have started savings groups to buy inputs together. But we would need to learn how to organize this."

One elder in the back says quietly, "The women's land access is the real problem, but that is... complicated."

What would you like to explore further?
""",
                        "positive_tracking": ["showed_listening", "asked_about_assets"]
                    },
                    "quick_solution": {
                        "keywords": ["should", "can bring", "will provide", "I know", "need to", "program", "fund", "donate", "give you"],
                        "reaction": """
The crowd is quiet for a moment. Chief Kofi exchanges glances with his council.

Ama speaks carefully: "These things sound interesting, but... forgive me, we have had visitors before with big ideas. The agricultural officer said fertilizer would solve everything, but we cannot buy it every season. The NGO brought seeds but left after one year, and we had no more seeds. The irrigation project - they built pumps but when they broke, no one could fix them."

An older woman adds, "Will this work continue when you return to America in two years?"

Kwame looks interested but concerned: "And the money to buy these things - where does it come from? Who will maintain them?"

Chief Kofi says diplomatically, "We appreciate your enthusiasm. But we must be practical. What happens after you leave?"

The energy in the meeting has shifted somewhat. People seem more guarded now.

How do you respond?
""",
                        "negative_tracking": ["jumped_to_solutions", "missed_sustainability"]
                    },
                    "sustainability_focus": {
                        "keywords": ["after I leave", "sustain", "continue", "maintain", "local resources", "community", "together", "organize"],
                        "reaction": """
Chief Kofi nods approvingly. "Now you speak with wisdom. Too many outsiders think they will save us and then disappear. We are tired of projects that die."

Ama becomes more animated: "Yes! If we are going to do something, it must be ours. We cannot depend on outside money forever. The women's cooperative - we started that ourselves. We meet, we support each other. If we learn new skills together, that knowledge stays here."

Kwame adds: "I have been reading about farmer-to-farmer teaching. If some of us learn good practices, we can teach others. The knowledge spreads without needing outside trainers forever. And if we use local resources - compost instead of expensive fertilizer, local seeds we can save and replant..."

An elder speaks: "My father grew seven types of yams. I remember only three. If we can remember this knowledge and mix it with new ideas..." He trails off, looking thoughtful.

Chief Kofi looks at you: "So you will work with us, not do things for us? This is good. But tell me - what is the first step? How do we begin?"

What do you propose as a first step?
""",
                        "positive_tracking": ["considered_sustainability", "showed_listening"]
                    },
                    "cultural_miss": {
                        "keywords": ["women should", "need to change", "traditional", "old ways", "backwards"],
                        "reaction": """
The atmosphere suddenly becomes tense. Several older men shift uncomfortably. Chief Kofi's expression becomes more formal and distant.

One elder says stiffly, "You have been here three months. We have been here our whole lives. Our ways have kept this community together through many hardships."

Ama, who moments ago seemed like your ally, looks uncomfortable. She glances at the men and says carefully, "The issues are... complex. Change must come from within, not from outside pushing."

Chief Kofi says diplomatically but firmly: "We thank you for your interest in our community. Perhaps we need more time to discuss these matters among ourselves first. We will call another meeting when we are ready."

The crowd begins to disperse, and you sense the evening's discussion is over - not productively.

As people leave, Kwame approaches quietly: "You touched on sensitive topics too directly. Even when change is needed, we must respect the process of how decisions are made here. May I offer some advice about how to approach this differently?"

How do you respond to Kwame?
""",
                        "negative_tracking": ["overlooked_culture"]
                    }
                }
            }
        },
        "peru": {
            "name": "Youth Education & Empowerment in Urban Peru",
            "description": "You're placed in a neighborhood on the outskirts of Lima where many young people drop out of school to help support their families. You'll work with a local community center, parents, and young people themselves to create opportunities that address their real needs.",
            "details": {
                "time_in_community": "2 months",
                "key_people": [
                    "Señora Rosa - Director of the community center, passionate but overworked, has been serving the community for 15 years",
                    "Miguel - 17-year-old who dropped out of school to work in construction, bright and articulate but feels he has no options",
                    "Carmen - Mother of three, works in the market, deeply worried about her children's future"
                ],
                "observations": "The neighborhood is vibrant with strong family ties and entrepreneurial spirit. Many families run small informal businesses. Young people are ambitious but face economic pressure and limited opportunities. The community center offers some after-school programs but struggles with funding and attendance.",
                "living_situation": "You rent a small apartment in the neighborhood and take the combi (minibus) around Lima like everyone else.",
                "sdg": "SDG 4: Quality Education - Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
                "cultural_considerations": [
                    "Family responsibility and contribution to household income is highly valued. Education that doesn't lead to immediate economic benefit can be seen as a luxury.",
                    "Machismo culture exists but is also being challenged by many families. Gender dynamics in education and work are complex."
                ]
            },
            "role_play": {
                "opening_scene": """
**BEGIN ROLE-PLAY**

You're at the community center on a Thursday evening. Señora Rosa invited you to a meeting with parents and some young people to discuss education challenges. About a dozen people sit in a circle in the center's main room.

Carmen speaks first, her voice tired but determined: "My oldest, he wants to continue school, but we need him to work. The market stall, it needs two people. My husband works long hours in the factory. What can I do? We need to eat."

Miguel, sitting in the back, adds: "Señora, with respect, school doesn't help anyway. I finished secondary school - and what? There are no jobs for people like us without connections. My cousin who went to university drives a taxi. At least in construction I earn money now."

Señora Rosa looks at you: "You see the problem we face? The young people are talented - Miguel is so smart - but they don't see a path forward. And the parents, they are not wrong about needing income. I have been thinking about this for years, but..." she trails off, looking overwhelmed.

A mother in the corner says: "The foreigners who came before, they gave scholarships to two students. Beautiful! But only two, and when the money stopped, that was it. What about everyone else?"

They all look at you expectantly.

What do you say or do?
""",
                "responses": {
                    "listening": {
                        "keywords": ["question", "ask", "learn", "tell me", "understand", "experience", "skills", "tried", "ideas", "dreams"],
                        "reaction": """
Miguel leans forward, seeming surprised to be asked: "What do I dream of? I mean... I liked learning. In school, I was good at mathematics and I liked building things with my hands. I thought maybe I could become an engineer or architect, but that's for rich kids from Miraflores, not for people from here."

Carmen nods vigorously: "My children are smart! But smart doesn't pay for food. If there was a way to learn AND earn, or to learn skills that lead directly to better work... but school is so general, you know?"

Señora Rosa brightens: "Actually, we do have resources people don't always remember. There's space in this center we barely use. Several parents have skills - Carmen, you know everything about running a business from your market stall. Jorge over there is an electrician. Maria does beautiful sewing and sells clothes."

A father in the corner adds: "The technical institute downtown has evening classes, but they cost money and the timing doesn't work for young people who work during the day."

Miguel says thoughtfully: "Some of my friends, we talk about starting businesses, but we don't know how. How to get permits, manage money, find customers... we just do what our parents showed us."

What direction would you like to explore?
""",
                        "positive_tracking": ["showed_listening", "asked_about_assets"]
                    },
                    "quick_solution": {
                        "keywords": ["should", "need to", "I will teach", "program", "bring in", "fund", "scholarship", "provide"],
                        "reaction": """
The room goes quiet. Carmen and the mother in the corner exchange knowing looks.

Señora Rosa says gently: "This sounds like many things we've heard before. The university students who came to tutor - they were here for three months for their service requirement, then gone. The scholarship program I mentioned - ran for two years, then funding ended. The computer training program - the laptops were donated but when they broke, we couldn't replace them."

Miguel says, a bit sharply: "No offense, but you'll go back to the United States in two years. Then what? Who teaches the classes then? Who pays for materials?"

Carmen adds more kindly: "You have a good heart, but we need something that doesn't depend on you or outside money. Something that is ours and continues."

A father says: "Also, being realistic - Miguel and young people like him work 10 hours a day, six days a week. When do they take classes? Evening? They're exhausted. Weekend? That's family time and their only rest."

The enthusiasm in the room has dampened. People look more skeptical now.

How do you respond to their concerns?
""",
                        "negative_tracking": ["jumped_to_solutions", "missed_sustainability"]
                    },
                    "sustainability_focus": {
                        "keywords": ["after I leave", "sustain", "continue", "community-led", "local resources", "peer", "each other"],
                        "reaction": """
Señora Rosa nods enthusiastically: "Exactly! This is what I've been thinking about. We have knowledge in this community. Maybe we don't use it well."

Carmen says: "I could teach young people about running a business - keeping accounts, dealing with suppliers, managing inventory. These are skills I use every day. If it helps them start their own work, I would be proud to teach."

The father who is an electrician speaks up: "I learned my trade through apprenticeship, working alongside my uncle. What if we did something similar? Young people could learn skills while earning a small amount, then teach others?"

Miguel looks interested now: "Like a network? Where we learn from people in the community, and as we get skilled, we help teach the next group? That could actually work long-term."

Señora Rosa adds: "The center has space we could use. And if we connect it to real economic opportunity - helping young people start micro-businesses, or qualifying for better jobs - parents can see the value."

A mother asks: "But how do we organize this? Who coordinates? Who makes sure quality is good? Who helps young people find customers or jobs after training?"

Miguel adds: "And honestly, we'd need some small startup money. Not forever, but to begin - materials, maybe small stipends while we learn so we can afford to work less for a few months..."

What do you suggest as next steps?
""",
                        "positive_tracking": ["considered_sustainability", "showed_listening"]
                    },
                    "cultural_miss": {
                        "keywords": ["should prioritize", "education is more important than", "need to change", "family shouldn't"],
                        "reaction": """
Carmen's face tightens. Several parents shift uncomfortably.

Carmen says, her voice harder now: "You think I don't value education? I work 12 hours a day so my children can eat and stay in school as long as possible. Don't tell me about priorities when you've never had to choose between your child's education and your child's dinner."

Señora Rosa intervenes diplomatically: "Different countries have different realities. Here, family economic survival is not optional. Young people who contribute to their families are showing responsibility and love, not making a mistake."

Miguel stands up, looking frustrated: "This is why programs from outside fail. You don't understand what life is actually like here. Not everyone can afford to think about the future when the present is hard enough."

An older father says quietly but firmly: "Our culture values family support. A son or daughter who helps their family is a good son or daughter. We are not wrong to expect this, and they are not wrong to provide it."

The meeting has taken an uncomfortable turn. People are withdrawing, less open now.

Señora Rosa says quietly to you: "Perhaps we should take a break. These are sensitive topics."

How do you respond?
""",
                        "negative_tracking": ["overlooked_culture"]
                    }
                }
            }
        },
        "philippines": {
            "name": "Clean Water & Environmental Health in Coastal Philippines",
            "description": "You're working with a fishing community that's facing challenges with clean water access and waste management. You'll collaborate with the barangay (village) council, fishermen's cooperative, and local health workers to develop solutions.",
            "details": {
                "time_in_community": "3 months",
                "key_people": [
                    "Captain Elena - Barangay captain (elected village leader), pragmatic and politically savvy, trying to balance many competing interests",
                    "Mang Tomas - Head of the fishermen's cooperative, weathered fisherman in his 50s, concerned about declining fish catches",
                    "Ate Lucia - Community health worker, sees the health impacts of water and sanitation issues daily"
                ],
                "observations": "The coastal community is tight-knit with strong family networks. Fishing has sustained families for generations but catches are declining. Many homes lack proper toilets, leading to beach contamination. Water comes from wells that are sometimes salty or contaminated. Trash accumulation is visible. Strong work ethic and community pride exist.",
                "living_situation": "You live with a host family in their home near the beach, sharing meals and participating in community life.",
                "sdg": "SDG 6: Clean Water and Sanitation - Ensure availability and sustainable management of water and sanitation for all",
                "cultural_considerations": [
                    "Filipino culture values 'pakikisama' (smooth interpersonal relationships) and 'hiya' (shame/propriety). Direct confrontation or criticism is avoided. Change happens through gentle persuasion and consensus.",
                    "The barangay captain and local officials have significant authority and influence. Working through proper channels is essential."
                ]
            },
            "role_play": {
                "opening_scene": """
**BEGIN ROLE-PLAY**

You're at the barangay hall for a regular community meeting. Captain Elena sits at the front table with council members. About 30 residents are present, sitting on benches. The smell of the ocean drifts through the open windows.

Ate Lucia stands to give a health report: "This month, we had 12 children with diarrhea, three serious cases. Also, skin infections are common. When I visit homes, I see the water from the wells is not always clean, and many families still do not have proper toilets."

Captain Elena nods seriously: "This is a problem, it's true. But building toilets is expensive. The families who need them most cannot afford them."

Mang Tomas adds: "And we have another problem connected to this - the trash. It goes into the ocean, and the fish are fewer every year. When we pull up nets, sometimes more plastic than fish. Our children, what will they catch when we are old?"

A mother in the audience says: "I boil water, but the fuel costs money. And where do we put trash? There is no collection here. We burn what we can, throw the rest in the sea like everyone has always done. What else can we do?"

Captain Elena looks at you: "You are the Peace Corps volunteer working on community development. Maybe you have seen how other places solve these problems? We would like to hear your thoughts."

Everyone turns to look at you with polite, expectant faces.

What do you say or do?
""",
                "responses": {
                    "listening": {
                        "keywords": ["question", "ask", "learn", "tell me", "understand", "tried", "ideas", "resources", "experience"],
                        "reaction": """
Captain Elena looks pleased that you're asking questions rather than jumping in with answers: "We tried to organize a clean-up day last year. Many people came, we filled many sacks with trash. But one week later, more trash appeared. No place to put it permanently, you see?"

Ate Lucia adds: "The province health office gave us water filters for five families, but there are 200 families here. And when the filters need replacement parts..." she shrugs.

Mang Tomas says: "Some fishermen talk about protected areas, give the fish space to breed. But we need to eat today, not just tomorrow. And if our barangay stops fishing in an area but the next barangay doesn't, we just lose income while they benefit."

A younger fisherman speaks up: "I have seen in Facebook videos about communities that recycle. They make money from trash! But I don't know how it works."

An older woman adds: "The toilets - some families have them. My cousin's house in the town has a septic system. But expensive to build, need cement, pipe, labor. And who knows how to build properly? One family tried, but it was not built right and now..." she makes a disgusted face.

Captain Elena says: "We have some budget from the municipality, but small. We have people willing to work. We have land if needed. But we need ideas that are practical for us."

What would you like to explore further?
""",
                        "positive_tracking": ["showed_listening", "asked_about_assets"]
                    },
                    "quick_solution": {
                        "keywords": ["should", "need to", "I will bring", "donate", "install", "provide", "buy for you"],
                        "reaction": """
The crowd is quiet and polite, but you notice people exchanging glances. Captain Elena maintains her smile but it seems more formal now.

Mang Tomas says carefully: "These sound like good technologies. But... when you return to America, who maintains them? When something breaks, who fixes it? We are fishermen, not engineers."

Ate Lucia adds gently: "We appreciate your generosity, but we have experience with donated things. The water filters I mentioned - when they need new parts, we cannot get them. The solar panels the NGO installed at the health center - one broke, and now they are just decoration."

A council member speaks up: "And the cost - if we become dependent on outside funding, what happens when it stops? We need solutions we can sustain ourselves."

A mother says: "My worry is maintenance. My neighbor has a water pump someone donated. When it broke after one year, no one could fix it. Now she carries water by bucket again, same as before, but more disappointed."

Captain Elena says diplomatically: "Your heart is kind, but we must be practical. We need to build something that is truly ours, that we understand and can continue. Otherwise, in three years, we are back to the same situation."

The energy in the room has shifted. People seem more guarded now, less enthusiastic.

How do you respond?
""",
                        "negative_tracking": ["jumped_to_solutions", "missed_sustainability"]
                    },
                    "sustainability_focus": {
                        "keywords": ["after I leave", "sustain", "local resources", "community-led", "maintain", "skills", "together"],
                        "reaction": """
Captain Elena smiles more genuinely: "Ah, now you speak practically! Yes, we need solutions that are ours. That we can do ourselves, even when you are gone."

Mang Tomas nods: "There are some among us with skills. Roberto can do carpentry and basic construction. Maria used to work at the town's water system. We know our own area - where water flows, where land is suitable, what materials are available nearby."

Ate Lucia says enthusiastically: "If we learn to build proper toilets ourselves, then we can help each other. Maybe start with a few demonstration houses, learn the technique, then spread the knowledge?"

The younger fisherman adds: "For the trash, what if we organize better? Some municipalities have waste segregation programs. Wet waste can become compost for gardens. Some plastic and metal can be sold to junk shops. We would need to organize collection and transport..."

Captain Elena says thoughtfully: "The barangay has a small budget. Not enough to give everyone free toilets, but maybe enough to buy materials at bulk discount, provide some subsidy, cover costs for poorest families? If community members provide labor to help each other?"

An older man says: "We have tradition of 'bayanihan' - community cooperation. If we decide together this is priority, we can organize work parties."

Captain Elena looks at you: "So, where do we start? What is the first step to move from talk to action?"

What do you propose as a first step?
""",
                        "positive_tracking": ["considered_sustainability", "showed_listening"]
                    },
                    "cultural_miss": {
                        "keywords": ["need to stop", "should change", "wrong way", "must make", "have to enforce"],
                        "reaction": """
The room goes very quiet. Several people suddenly find the floor very interesting. The warm, open atmosphere has become tense.

Captain Elena's smile becomes fixed and formal: "I see. These are... strong suggestions." Her tone is still polite, but noticeably cooler.

An older council member says carefully: "Perhaps our way of doing things seems strange to foreigners. But there are reasons for how we live. Change is not simple."

Mang Tomas says, more directly: "You have been here three months. We have been here our whole lives. We are not children needing to be scolded."

Ate Lucia looks uncomfortable, glancing between you and the community members: "There are many factors to consider... culture, economics, beliefs..."

A few people start quietly getting up and leaving. Others are whispering to each other, looking uncomfortable.

Captain Elena says with diplomatic finality: "Thank you for your input. We will think carefully about these matters and discuss among ourselves. Perhaps we will meet again when we have had time to consider." This is clearly a polite dismissal.

As the meeting breaks up, Ate Lucia approaches you quietly: "You may want to be more careful about how you present ideas. In our culture, direct criticism causes people to lose face. Even if change is needed, it must happen in a way that preserves dignity and shows respect for local knowledge."

How do you respond to Ate Lucia?
""",
                        "negative_tracking": ["overlooked_culture"]
                    }
                }
            }
        }
    }

    @classmethod
    def get_scenario(cls, scenario_id: str) -> dict:
        """Get scenario data by ID"""
        return cls.SCENARIOS.get(scenario_id, {})


class PeaceCorpsGame:
    """Main game engine"""

    def __init__(self):
        self.state = GameState()
        self.scenarios = ScenarioData()

    def display(self, text: str):
        """Display text to player"""
        print(f"\n{text}\n")
        print("=" * 80)

    def get_input(self, prompt: str = "\nYour response: ") -> str:
        """Get input from player"""
        return input(prompt).strip()

    def save_game(self, filename: str = "save_game.json"):
        """Save game state"""
        save_data = {
            "phase": self.state.phase.value,
            "player": {
                "background_knowledge": self.state.player.background_knowledge,
                "interests": self.state.player.interests,
                "chosen_scenario": self.state.player.chosen_scenario
            },
            "turn_count": self.state.turn_count,
            "conversation_history": self.state.conversation_history,
            "player_actions": self.state.player_actions,
            "tracking": {
                "showed_listening": self.state.showed_listening,
                "asked_about_assets": self.state.asked_about_assets,
                "considered_sustainability": self.state.considered_sustainability,
                "showed_cultural_sensitivity": self.state.showed_cultural_sensitivity,
                "jumped_to_solutions": self.state.jumped_to_solutions,
                "missed_sustainability": self.state.missed_sustainability,
                "overlooked_culture": self.state.overlooked_culture,
                "ignored_existing_strengths": self.state.ignored_existing_strengths
            }
        }

        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=2)

    def load_game(self, filename: str = "save_game.json") -> bool:
        """Load game state"""
        if not os.path.exists(filename):
            return False

        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)

            self.state.phase = GamePhase(save_data["phase"])
            self.state.player.background_knowledge = save_data["player"]["background_knowledge"]
            self.state.player.interests = save_data["player"]["interests"]
            self.state.player.chosen_scenario = save_data["player"]["chosen_scenario"]
            self.state.turn_count = save_data["turn_count"]
            self.state.conversation_history = save_data["conversation_history"]
            self.state.player_actions = save_data["player_actions"]

            tracking = save_data["tracking"]
            self.state.showed_listening = tracking["showed_listening"]
            self.state.asked_about_assets = tracking["asked_about_assets"]
            self.state.considered_sustainability = tracking["considered_sustainability"]
            self.state.showed_cultural_sensitivity = tracking["showed_cultural_sensitivity"]
            self.state.jumped_to_solutions = tracking["jumped_to_solutions"]
            self.state.missed_sustainability = tracking["missed_sustainability"]
            self.state.overlooked_culture = tracking["overlooked_culture"]
            self.state.ignored_existing_strengths = tracking["ignored_existing_strengths"]

            return True
        except Exception as e:
            print(f"Error loading game: {e}")
            return False

    def run(self):
        """Main game loop"""
        # Check for saved game
        if os.path.exists("save_game.json"):
            response = input("Found a saved game. Continue? (y/n): ").strip().lower()
            if response == 'y':
                if self.load_game():
                    print("\nGame loaded successfully!")
                else:
                    print("\nCouldn't load game. Starting new game.")
                    self.state = GameState()

        while self.state.phase != GamePhase.COMPLETE:
            if self.state.phase == GamePhase.INTRO:
                self.intro_phase()
            elif self.state.phase == GamePhase.SCENARIO_SELECTION:
                self.scenario_selection_phase()
            elif self.state.phase == GamePhase.SCENARIO_DETAILS:
                self.scenario_details_phase()
            elif self.state.phase == GamePhase.ROLE_PLAY:
                self.role_play_phase()
            elif self.state.phase == GamePhase.DECISION_POINT:
                self.decision_point_phase()
            elif self.state.phase == GamePhase.FEEDBACK:
                self.feedback_phase()

            # Auto-save after each phase
            self.save_game()

        self.display("Thank you for playing the Peace Corps Social Entrepreneurship Simulation!")

    def intro_phase(self):
        """Handle introduction and player background"""
        self.display("""
Hello! I'm your AI Mentor, and I'm excited to help you explore what it's like to be
a Peace Corps Volunteer working on sustainable development. In this simulation,
you'll experience the real challenges and rewards of working with a community to
create positive change that lasts.

Before we begin, I'd like to understand a bit about you so I can tailor this experience:

- Have you learned about international development, social entrepreneurship, or
  the Peace Corps before? If so, what do you already know?
- What interests you most about helping communities create sustainable change?

Please share whatever feels relevant - there are no wrong answers!
        """)

        response = self.get_input()
        self.state.player.background_knowledge = response
        self.state.conversation_history.append({
            "speaker": "player",
            "phase": "intro",
            "content": response
        })

        self.state.phase = GamePhase.SCENARIO_SELECTION

    def scenario_selection_phase(self):
        """Handle scenario selection"""
        self.display("""
Great! Based on what you've shared, I'm going to offer you three different Peace Corps
scenarios. Each one will challenge you to build relationships, understand community needs,
and design a project that can sustain itself long after you leave.

Pick whichever sounds most interesting to you:

**Option 1: Agricultural Development in Rural Ghana**
You're assigned to a small farming village that's been struggling with food security.
The community grows cocoa for export but has difficulty growing enough food for themselves.
You'll work with local farmers, women's groups, and the village chief to explore sustainable
solutions.

**Option 2: Youth Education & Empowerment in Urban Peru**
You're placed in a neighborhood on the outskirts of Lima where many young people drop out
of school to help support their families. You'll work with a local community center, parents,
and young people themselves to create opportunities that address their real needs.

**Option 3: Clean Water & Environmental Health in Coastal Philippines**
You're working with a fishing community that's facing challenges with clean water access
and waste management. You'll collaborate with the barangay (village) council, fishermen's
cooperative, and local health workers to develop solutions.

Which scenario would you like to explore? (Type 1, 2, or 3)
        """)

        while True:
            response = self.get_input()

            if response in ["1", "one", "ghana", "option 1"]:
                self.state.player.chosen_scenario = "ghana"
                break
            elif response in ["2", "two", "peru", "option 2"]:
                self.state.player.chosen_scenario = "peru"
                break
            elif response in ["3", "three", "philippines", "option 3"]:
                self.state.player.chosen_scenario = "philippines"
                break
            else:
                print("Please enter 1, 2, or 3 to choose your scenario.")

        self.state.conversation_history.append({
            "speaker": "player",
            "phase": "scenario_selection",
            "content": f"Chose scenario: {self.state.player.chosen_scenario}"
        })

        self.state.phase = GamePhase.SCENARIO_DETAILS

    def scenario_details_phase(self):
        """Display scenario details"""
        scenario = self.scenarios.get_scenario(self.state.player.chosen_scenario)
        details = scenario["details"]

        key_people_text = "\n".join([f"   • {person}" for person in details["key_people"]])
        cultural_text = "\n".join([f"   • {consideration}" for consideration in details["cultural_considerations"]])

        self.display(f"""
**{scenario['name']}**

**Your Situation:**
• Time in community: {details['time_in_community']}
• Living situation: {details['living_situation']}

**Key People You've Met:**
{key_people_text}

**What You've Observed:**
{details['observations']}

**Relevant UN Sustainable Development Goal:**
{details['sdg']}

**Your Goal:**
Design a sustainable development project that:
• Addresses a real need the community has identified
• Can continue after you leave (sustainability is core, not an add-on)
• Builds on existing community strengths and resources
• Respects local culture and power dynamics

**What You Have:**
• A small budget for materials (not ongoing salaries)
• Your skills and the ability to provide training
• 2 years of service time
• Connections to other Peace Corps volunteers and some local NGOs

**Important Cultural Context:**
{cultural_text}

Press Enter when you're ready to begin the role-play...
        """)

        self.get_input("")
        self.state.phase = GamePhase.ROLE_PLAY

    def role_play_phase(self):
        """Handle role-play interaction"""
        scenario = self.scenarios.get_scenario(self.state.player.chosen_scenario)

        # First turn - show opening scene
        if self.state.turn_count == 0:
            self.display(scenario["role_play"]["opening_scene"])

        # Get player response
        player_response = self.get_input()
        self.state.conversation_history.append({
            "speaker": "player",
            "phase": "role_play",
            "content": player_response
        })
        self.state.player_actions.append(player_response)

        # Analyze response and provide appropriate reaction
        response_type = self.analyze_response(player_response)
        npc_response = scenario["role_play"]["responses"][response_type]["reaction"]

        # Update tracking
        if "positive_tracking" in scenario["role_play"]["responses"][response_type]:
            for trait in scenario["role_play"]["responses"][response_type]["positive_tracking"]:
                setattr(self.state, trait, True)

        if "negative_tracking" in scenario["role_play"]["responses"][response_type]:
            for trait in scenario["role_play"]["responses"][response_type]["negative_tracking"]:
                setattr(self.state, trait, True)

        self.display(npc_response)

        self.state.conversation_history.append({
            "speaker": "npc",
            "phase": "role_play",
            "content": npc_response
        })

        self.state.turn_count += 1

        # After 3 meaningful exchanges, move to decision point
        if self.state.turn_count >= 3:
            self.state.phase = GamePhase.DECISION_POINT

    def analyze_response(self, response: str) -> str:
        """Analyze player response to determine type"""
        response_lower = response.lower()
        scenario = self.scenarios.get_scenario(self.state.player.chosen_scenario)
        responses_data = scenario["role_play"]["responses"]

        # Check each response type for keyword matches
        scores = {}
        for response_type, data in responses_data.items():
            if "keywords" in data:
                score = sum(1 for keyword in data["keywords"] if keyword in response_lower)
                scores[response_type] = score

        # Return type with highest score, or default to listening if no clear match
        if scores:
            max_score = max(scores.values())
            if max_score > 0:
                return max(scores, key=scores.get)

        # Default to listening response
        return "listening"

    def decision_point_phase(self):
        """Present a key decision point"""
        scenario_id = self.state.player.chosen_scenario

        if scenario_id == "ghana":
            decision_text = """
The community meeting continues. Chief Kofi says: "We have talked much, and this is good.
But now we must decide on action. I see two paths before us:

**Path 1:** Start with a pilot project - work with Ama's women's cooperative to trial
improved food crop techniques on their small plots. Learn what works, document it, then
expand to others. This is slower but lower risk.

**Path 2:** Organize a community-wide initiative immediately - bring together farmers,
women's groups, and elders to plan a comprehensive food security program. This could create
bigger impact faster but requires mobilizing many people and resources at once.

You are our partner in this work. Which path do you think we should take, and why?"

Which path do you choose, and what is your reasoning?
            """
        elif scenario_id == "peru":
            decision_text = """
Señora Rosa says: "We have been discussing many good ideas. But we must choose where to
start. I see two possible approaches:

**Path 1:** Begin with a pilot skills training program for 10-15 young people. Focus on
quality, build a strong model, learn what works, then expand. Partner with local artisans
and business owners who can provide mentorship.

**Path 2:** Create a broader youth empowerment center right away - offer various activities
(skills training, tutoring, entrepreneurship support) and let young people choose what they
need most. Cast a wider net to reach more young people immediately.

Miguel, what do you think? And others, your opinions?"

Everyone looks to you for guidance.

Which path do you think is better, and why?
            """
        else:  # philippines
            decision_text = """
Captain Elena says: "We have discussed much today. Now we must decide how to move forward.
I see two approaches:

**Path 1:** Start with a bayanihan work project - choose 5-10 households that need toilets
most urgently, organize community work parties to build them together while learning proper
techniques. Create a demonstration that others can see and learn from.

**Path 2:** Begin with community education and waste management - organize the whole barangay
in a waste segregation and recycling program first. This addresses the immediate visible
problem and builds community organizing skills, then leverage that success for the toilet
project later.

Mang Tomas, Ate Lucia, what do you think? And you, our Peace Corps friend, which approach
makes more sense?"

The room looks to you for input.

Which path do you recommend, and what is your reasoning?
            """

        self.display(decision_text)

        player_decision = self.get_input()
        self.state.conversation_history.append({
            "speaker": "player",
            "phase": "decision",
            "content": player_decision
        })

        # Show consequence of decision
        consequence_text = self.generate_consequence(player_decision)
        self.display(consequence_text)

        self.display("\n**END OF ROLE-PLAY**\n")

        self.state.phase = GamePhase.FEEDBACK

    def generate_consequence(self, decision: str) -> str:
        """Generate consequence based on decision"""
        decision_lower = decision.lower()

        # Simple consequence based on whether they chose path 1 or 2
        # and whether they justified it with sustainable thinking

        if "1" in decision_lower or "first" in decision_lower or "pilot" in decision_lower:
            if any(word in decision_lower for word in ["learn", "test", "risk", "quality", "demonstrate"]):
                return """
The community members nod approvingly. Chief Kofi/Señora Rosa/Captain Elena says:
"This shows wisdom - start small, learn well, then grow. This is how sustainable
change happens. Let us begin planning the pilot project together."

People begin discussing concrete next steps with enthusiasm and practical focus.
                """
            else:
                return """
The community accepts this path but seems uncertain. Mang Tomas/Miguel/Ama asks:
"Why start small? What will we learn that we don't know?" You realize you might
need to better articulate the value of the pilot approach to build genuine buy-in.
                """
        elif "2" in decision_lower or "second" in decision_lower or "broader" in decision_lower or "comprehensive" in decision_lower:
            if any(word in decision_lower for word in ["momentum", "mobilize", "together", "capacity", "visible"]):
                return """
The community members look energized. "Yes! If we all work together, we can make
real change!" However, Chief Kofi/Señora Rosa/Captain Elena adds cautiously:
"This is ambitious. We must be careful to organize well so we don't start strong
but finish weak. Let us plan carefully."

People begin discussing logistics with a mix of excitement and concern about
sustainability.
                """
            else:
                return """
Some community members look excited, but others appear worried. An elder says:
"This is very much, very fast. What if we cannot sustain it?" You sense that
the community might need more reassurance about how this larger initiative can
remain viable long-term.
                """
        else:
            return """
The community listens politely to your reasoning. Chief Kofi/Señora Rosa/Captain Elena
says: "These are interesting thoughts. Let us take time to consider all perspectives
and meet again soon." The meeting concludes with uncertainty about next steps.
            """

    def feedback_phase(self):
        """Provide feedback and reflection"""
        self.display("""
Welcome back! Let's reflect on how that went. You made some interesting choices,
and I want to highlight both your strengths and areas for growth.
        """)

        # Generate strengths feedback
        strengths = []
        if self.state.showed_listening:
            strengths.append("• **Active Listening:** You asked questions to understand the situation before proposing solutions. This is exactly what effective Peace Corps volunteers do - listen first, propose later.")
        if self.state.asked_about_assets:
            strengths.append("• **Asset-Based Approach:** You asked about what the community already has - their skills, knowledge, and resources. This shows you understand that communities aren't problems to be solved, but partners with existing strengths.")
        if self.state.considered_sustainability:
            strengths.append("• **Sustainability Focus:** You thought about what happens after you leave. This is crucial - the best development projects don't depend on the volunteer's continued presence.")
        if self.state.showed_cultural_sensitivity:
            strengths.append("• **Cultural Awareness:** You showed sensitivity to local culture, power dynamics, and decision-making processes.")

        if not strengths:
            strengths.append("• **Willingness to Engage:** You participated authentically in a complex scenario. This kind of engagement is the first step toward becoming an effective development practitioner.")

        # Generate growth areas feedback
        growth_areas = []
        if self.state.jumped_to_solutions:
            growth_areas.append("""
• **Patience with Problem Understanding:** I noticed you proposed solutions relatively quickly.
  In real Peace Corps work, volunteers often spend their first 3-6 months just listening and
  building relationships. Consider: What might you have learned if you'd asked more questions
  before suggesting answers? What assumptions might you have made about the community's needs
  without fully understanding their perspective?
            """)
        if self.state.missed_sustainability:
            growth_areas.append("""
• **Long-Term Thinking:** Some of your ideas relied on ongoing outside resources or your
  continued presence. Ask yourself: "What happens when I leave in 2 years?" If the answer
  is "the project stops," it's not truly sustainable. The best projects use local resources,
  build local skills, and can be maintained by the community indefinitely.
            """)
        if self.state.overlooked_culture:
            growth_areas.append("""
• **Cultural Humility:** You touched on some culturally sensitive topics in ways that may
  have caused community members to withdraw. Remember: power dynamics, gender roles, and
  decision-making processes vary widely across cultures. Change is possible, but it must
  come from within the community, not imposed from outside. Your role is to support, not
  to push.
            """)
        if self.state.ignored_existing_strengths:
            growth_areas.append("""
• **Building on What Exists:** The community mentioned existing resources, knowledge, and
  skills that you didn't fully explore. Communities aren't empty vessels waiting for outside
  help - they have knowledge systems, social structures, and solutions that have sustained
  them for generations. The most effective projects amplify what's already there rather than
  starting from scratch.
            """)

        if not growth_areas:
            growth_areas.append("""
• **Deepening Engagement:** While you showed good instincts, consider how you might deepen
  your engagement. Could you have asked follow-up questions? Explored community assets more?
  Checked your assumptions more explicitly? There's always room to listen more deeply.
            """)

        # Display feedback
        if strengths:
            self.display("**What You Did Well:**\n\n" + "\n\n".join(strengths))

        if growth_areas:
            self.display("**Areas to Consider:**\n\n" + "\n\n".join(growth_areas))

        # Key takeaways
        self.display("""
**Key Takeaways for Future Development Work:**

1. **Community needs assessment comes first** - Spend time listening, observing, and asking
   questions before proposing any solutions. The best projects address needs the community
   has identified, not needs you assume they have.

2. **Sustainability must be built in from the start** - Ask yourself: "What happens when I
   leave?" If the answer is "the project stops," it's not sustainable. Design projects that
   use local resources, build local skills, and can be maintained by the community.

3. **Build on existing strengths** - Communities aren't empty vessels waiting for help. They
   have knowledge, resources, relationships, and often existing solutions. Your role is to
   support and amplify what's already there.

4. **Cultural humility is essential** - Power dynamics, gender roles, decision-making processes,
   and communication styles vary widely. Take time to understand and respect local culture
   rather than imposing outside approaches.

5. **Relationships are the foundation** - Trust takes time to build. The most successful Peace
   Corps projects often happen in the second year of service, after relationships are established.

**Peace Corps Service:**
Real Peace Corps volunteers spend 27 months in their communities (3 months training + 24 months
service). They work in sectors including education, health, agriculture, environment, youth
development, and community economic development. The experience is challenging but transformative
- volunteers consistently report that they learned more from their communities than they gave.

If you're interested in learning more about Peace Corps service, visit: www.peacecorps.gov
        """)

        # Offer to play again
        self.display("Would you like to try another scenario? (yes/no)")
        response = self.get_input().lower()

        if response in ["yes", "y", "yeah", "sure"]:
            # Reset for new game
            self.state = GameState()
            self.state.phase = GamePhase.INTRO
            if os.path.exists("save_game.json"):
                os.remove("save_game.json")
        else:
            self.state.phase = GamePhase.COMPLETE


def main():
    """Entry point"""
    print("\n" + "=" * 80)
    print("PEACE CORPS SOCIAL ENTREPRENEURSHIP SIMULATION")
    print("A Turn-Based Educational Game")
    print("=" * 80)

    game = PeaceCorpsGame()
    game.run()


if __name__ == "__main__":
    main()
