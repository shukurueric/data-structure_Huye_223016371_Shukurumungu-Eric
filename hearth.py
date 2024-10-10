from collections import deque

class HealthInsuranceClaims:
    def __init__(self):
        self.claim_stack = []  # Stack for undoing claims
        self.claim_queue = deque()  # Queue for processing claims
        self.claim_history = []  # List for tracking claim history

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
            self.claim_stack.append(claim)  # Add to stack for potential undo
        else:
            print("No claims to process.")

    def undo_last_claim(self):
        """Undo the last processed claim."""
        if self.claim_stack:
            claim = self.claim_stack.pop()
            self.claim_queue.appendleft(claim)  # Re-add to queue
            print(f"Undo claim: {claim}")
        else:
            print("No claims to undo.")

    def view_claim_history(self):
        """View the history of all claims filed."""
        print("Claim history:")
        for claim in self.claim_history:
            print(claim)

# Example usage
if __name__ == "__main__":
    claims_system = HealthInsuranceClaims()

    # Filing claims
    claims_system.file_claim("Claim #1: Broken Arm")
    claims_system.file_claim("Claim #2: Flu Treatment")
    
    # Processing claims
    claims_system.process_claim()  # Process Claim #1
    claims_system.process_claim()  # Process Claim #2
    
    # Undo last claim
    claims_system.undo_last_claim()  # Undo Claim #2
    
    # View claim history
    claims_system.view_claim_history()
