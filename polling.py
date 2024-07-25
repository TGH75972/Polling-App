class Poll:
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.votes = [0] * len(options)

    def vote(self, option_index):
        if 0 <= option_index < len(self.options):
            self.votes[option_index] += 1
        else:
            print("Invalid option index.")

    def get_results(self):
        return list(zip(self.options, self.votes))

class PollSystem:
    def __init__(self):
        self.polls = []

    def create_poll(self):
        question = input("Enter the poll question: ")
        options = []
        print("Enter options for the poll. Type 'done' when finished.")
        while True:
            option = input("Option: ")
            if option.lower() == 'done':
                if len(options) < 2:
                    print("A poll must have at least two options. Please add more options.")
                else:
                    break
            else:
                options.append(option)

        poll = Poll(question, options)
        self.polls.append(poll)
        print("Poll created successfully.")

    def vote(self):
        if not self.polls:
            print("No polls available.")
            return

        print("Available polls:")
        for i, poll in enumerate(self.polls):
            print(f"{i + 1}. {poll.question}")

        try:
            poll_index = int(input("Enter the number of the poll you want to vote on: ")) - 1
            if not (0 <= poll_index < len(self.polls)):
                print("Invalid poll number.")
                return

            poll = self.polls[poll_index]
            print("Options:")
            for i, option in enumerate(poll.options):
                print(f"{i + 1}. {option}")

            option_index = int(input("Enter the number of the option you want to vote for: ")) - 1
            poll.vote(option_index)
            print("Vote cast successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_results(self):
        if not self.polls:
            print("No polls available.")
            return

        print("Available polls:")
        for i, poll in enumerate(self.polls):
            print(f"{i + 1}. {poll.question}")

        try:
            poll_index = int(input("Enter the number of the poll you want to view results for: ")) - 1
            if not (0 <= poll_index < len(self.polls)):
                print("Invalid poll number.")
                return

            poll = self.polls[poll_index]
            results = poll.get_results()
            print("Results:")
            for option, votes in results:
                print(f"{option}: {votes} votes")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    poll_system = PollSystem()

    while True:
        print("\nPoll System Menu:")
        print("1. Create Poll")
        print("2. Vote")
        print("3. View Results")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                poll_system.create_poll()
            elif choice == 2:
                poll_system.vote()
            elif choice == 3:
                poll_system.view_results()
            elif choice == 4:
                print("Exiting the Poll System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
