from collections import deque

class HealthInsuranceClaims:
    def __init__(self):
        self.claim_stack = []  
        self.claim_queue = deque()  
        self.claim_history = []  
    def file_claim(self, claim):
        """File a new claim and add it to the queue."""
        self.claim_queue.append(claim)
        self.claim_history.append(claim)
        print(f"Claim filed: {claim}")

    def process_claim(self):
        """Process the next claim in the queue."""
        if self.claim_queue:
            claim = self.claim_queue.popleft()
            print(f"Processing claim: {claim}")
            self.claim_stack.append(claim)  
        else:
            print("No claims to process.")

    def undo_last_claim(self):
        """Undo the last processed claim."""
        if self.claim_stack:
            claim = self.claim_stack.pop()
            self.claim_queue.appendleft(claim)  
            print(f"Undo claim: {claim}")
        else:
            print("No claims to undo.")

    def view_claim_history(self):
        """View the history of all claims filed."""
        print("Claim history:")
        for claim in self.claim_history:
            print(claim)


if __name__ == "__main__":
    claims_system = HealthInsuranceClaims()

    
    claims_system.file_claim("Claim #1: Broken Arm")
    claims_system.file_claim("Claim #2: Flu Treatment")
    
    
    claims_system.process_claim()  
    claims_system.process_claim()  

    claims_system.undo_last_claim()  
    
    
    claims_system.view_claim_history()
