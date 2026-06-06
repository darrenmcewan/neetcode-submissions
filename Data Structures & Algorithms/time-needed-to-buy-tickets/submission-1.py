class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        ticket_customers = [(i,cnt) for i,cnt in enumerate(tickets)]
        while True:
            customer, ticket_cnt = ticket_customers.pop(0)
            time+=1
            if customer == k and ticket_cnt == 1:
                return time
            if ticket_cnt > 1:
                ticket_customers.append((customer,ticket_cnt-1))
            
        