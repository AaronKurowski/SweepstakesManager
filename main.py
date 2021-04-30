from marketingfirmcreator import MarketingFirmCreator
from user_interface import continue_prompt, get_sweepstakes_name, select_winner_prompt
from contestant import Contestant


if __name__ == '__main__':
    def run_simulation():
        my_manager = MarketingFirmCreator().choose_manager_type()
        """Creates new sweepstakes"""
        while True:
            new_sweepstakes_name = get_sweepstakes_name()
            new_sweepstakes = my_manager.create_sweepstakes(new_sweepstakes_name)
            my_manager.manager.insert_sweepstakes(new_sweepstakes)

            while True:
                print("Enter Contestant:\n")
                contestant = Contestant()
                contestant.fill_contestant_info()
                new_sweepstakes.register_contestant(contestant)
                print("Contestant registered")
                add_more_contestants = continue_prompt()
                if add_more_contestants.lower() == 'y' or add_more_contestants.lower() == 'yes':
                    continue
                else:
                    break
            print("\nSweepstakes:")
            add_another_sweepstakes = continue_prompt()
            if add_another_sweepstakes.lower() == 'y' or add_another_sweepstakes.lower() == 'yes':
                continue
            else:
                break

        select_winner = select_winner_prompt()
        while select_winner:
            try:
                selected_sweepstakes = my_manager.manager.get_sweepstakes()
                winner = selected_sweepstakes.pick_winner()
                winner.notify(winner, selected_sweepstakes)
            except AttributeError:
                break

    run_simulation()
