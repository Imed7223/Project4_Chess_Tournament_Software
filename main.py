from views.menu import MenuView
from controllers.controller_tournament import TournamentController


def run():
    controller = TournamentController()
    controller.save_tournaments_to_json("tournaments.json")
    # Charger les tournois
    controller.load_tournaments_from_json("tournaments.json")
    while True:
        MenuView.display_message(MenuView.afficher_menu_principal())
        choice = MenuView.get_choice()
        if choice == "1":
            controller.add_new_tournament()
        elif choice == "2":
            controller.select_a_tournament()
        elif choice == "3":
            controller.selected_players()
            controller.save_tournaments_to_json()
        elif choice == "4":
            controller.playing_rounds()
            controller.save_tournaments_to_json()
        elif choice == "5":
            controller.selected_tournament_details()
        elif choice == "6":
            controller.details_all_tournaments_rounds_and_matchs()
        elif choice == "7":
            controller.display_ranking_players()
            controller.save_tournaments_to_json()
        elif choice == "8":
            controller.ordered_candidates_players_list()
        elif choice == "9":
            controller.ordered_all_tournament_players_list()
        elif choice == "10":
            controller.display_tournaments()
        elif choice == "11":
            MenuView.display_message("Bye !")
            break
        else:
            MenuView.display_message("Invalid choice.")


if __name__ == "__main__":
    run()
