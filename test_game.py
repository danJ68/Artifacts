#!/usr/bin/env python3
"""
Quick test script to verify the Peace Corps game works
"""

import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from peace_corps_game import PeaceCorpsGame, GamePhase, ScenarioData

def test_game_initialization():
    """Test that the game initializes correctly"""
    print("Testing game initialization...")
    game = PeaceCorpsGame()
    assert game.state.phase == GamePhase.INTRO, "Game should start in INTRO phase"
    print("✓ Game initialization successful")

def test_scenario_data():
    """Test that scenario data is properly loaded"""
    print("\nTesting scenario data...")
    scenarios = ScenarioData()

    # Test Ghana scenario
    ghana = scenarios.get_scenario("ghana")
    assert ghana is not None, "Ghana scenario should exist"
    assert "name" in ghana, "Ghana scenario should have a name"
    assert "details" in ghana, "Ghana scenario should have details"
    assert "role_play" in ghana, "Ghana scenario should have role_play data"
    print("✓ Ghana scenario loaded")

    # Test Peru scenario
    peru = scenarios.get_scenario("peru")
    assert peru is not None, "Peru scenario should exist"
    assert "name" in peru, "Peru scenario should have a name"
    print("✓ Peru scenario loaded")

    # Test Philippines scenario
    philippines = scenarios.get_scenario("philippines")
    assert philippines is not None, "Philippines scenario should exist"
    assert "name" in philippines, "Philippines scenario should have a name"
    print("✓ Philippines scenario loaded")

def test_response_analysis():
    """Test response analysis system"""
    print("\nTesting response analysis...")
    game = PeaceCorpsGame()
    game.state.player.chosen_scenario = "ghana"

    # Test listening response
    listening_response = "I'd like to learn more about what you've already tried. What are your thoughts?"
    response_type = game.analyze_response(listening_response)
    assert response_type == "listening", f"Should detect listening response, got {response_type}"
    print("✓ Listening response detected")

    # Test quick solution response
    solution_response = "I think we should bring in new fertilizers and I can provide training"
    response_type = game.analyze_response(solution_response)
    assert response_type == "quick_solution", f"Should detect quick solution, got {response_type}"
    print("✓ Quick solution response detected")

    # Test sustainability response
    sustain_response = "What can continue after I leave? Let's use local resources and organize together"
    response_type = game.analyze_response(sustain_response)
    assert response_type == "sustainability_focus", f"Should detect sustainability focus, got {response_type}"
    print("✓ Sustainability response detected")

def test_save_load():
    """Test save and load functionality"""
    print("\nTesting save/load functionality...")

    # Clean up any existing save file
    if os.path.exists("save_game.json"):
        os.remove("save_game.json")

    # Create a game and modify state
    game1 = PeaceCorpsGame()
    game1.state.phase = GamePhase.SCENARIO_SELECTION
    game1.state.player.background_knowledge = "Test knowledge"
    game1.state.player.interests = "Test interests"
    game1.state.turn_count = 5
    game1.state.showed_listening = True

    # Save the game
    game1.save_game()
    assert os.path.exists("save_game.json"), "Save file should be created"
    print("✓ Game saved successfully")

    # Load into a new game instance
    game2 = PeaceCorpsGame()
    loaded = game2.load_game()
    assert loaded, "Game should load successfully"
    assert game2.state.phase == GamePhase.SCENARIO_SELECTION, "Phase should be restored"
    assert game2.state.player.background_knowledge == "Test knowledge", "Player data should be restored"
    assert game2.state.turn_count == 5, "Turn count should be restored"
    assert game2.state.showed_listening == True, "Tracking data should be restored"
    print("✓ Game loaded successfully")

    # Clean up
    os.remove("save_game.json")
    print("✓ Save file cleaned up")

def run_all_tests():
    """Run all tests"""
    print("=" * 80)
    print("PEACE CORPS GAME - TEST SUITE")
    print("=" * 80)

    try:
        test_game_initialization()
        test_scenario_data()
        test_response_analysis()
        test_save_load()

        print("\n" + "=" * 80)
        print("ALL TESTS PASSED ✓")
        print("=" * 80)
        return True

    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
