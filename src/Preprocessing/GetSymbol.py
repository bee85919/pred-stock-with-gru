import os
from Utils.envLoader import envLoader


pth = envLoader().get_path().get


class GetSymbol:

    def __init__(self, data):
        print("Getting symbols...")
        syms, size = self.get_syms(data)
        self.save_syms(syms, size)
        

    def get_syms(self, data):
        syms = data['symbol'].unique().tolist()
        syms_batched = [syms[i:i + 100] for i in range(0, len(syms), 100)]
        return syms_batched, len(syms)
    
    
    def save_syms(self, syms, size):        
        print(f"Save total symbols: {len(syms)}")   
        with open(pth('syms'), 'w') as f: f.write(str(syms))
        print(f"Save batches' cnt: {len(size)}")
        with open(pth('batch_cnt'), 'w') as f: f.write(str(size))