from stack_overflow import StackOverflow
class StackOverflowDemo:
    @staticmethod
    def run():
        system = StackOverflow()

        alice = system.create_user("alice", "alice@gmail.com")
        bob   = system.create_user("bob", "bob@example.com")
        charlie = system.create_user("charlie", "charlie@example.com")

        # ALcie asks a questions

        java_question = system.ask_question(alice, "polymorphism in java", 
                                            "Can someone explain this? ", ["java", "oop"])
        
        bob_answer = system.answer_question(bob, java_question, "it's ability to take different forms")

        # Charlie comments on the question

        charlie_comment = system.add_comment(charlie, java_question, "Good question! I am also interested to learn more about this.")


        # Alice comments on bob_answer
        alice_comment = system.add_comment(alice, bob_answer, "Thanks for exaplaining")

        # Charlie votes the question and answer
        system.vote_question(charlie, java_question, 1)
        system.vote_answer(charlie, bob_answer, 1)

        system.accept_answer(bob_answer)


if __name__ == "__main__":
    StackOverflowDemo.run()