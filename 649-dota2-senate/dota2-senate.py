class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue = []
        dQueue = []
    
        for i, s in enumerate(senate):
            if s == 'R':
                rQueue.append(i)
            else:
                dQueue.append(i)
        
        while rQueue and dQueue:
            rQueueIndex = rQueue.pop(0)
            dQueueIndex = dQueue.pop(0)

            if rQueueIndex < dQueueIndex:
                rQueue.append(rQueueIndex + len(senate))
            else:
                dQueue.append(dQueueIndex + len(senate))
        
        if rQueue:
            return 'Radiant'
        else:
            return 'Dire'