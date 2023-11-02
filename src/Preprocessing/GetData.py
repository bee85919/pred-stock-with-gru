import os
import pandas as pd
from Utils.envLoader import envLoader
from Utils.createDir import createDir


pth = envLoader().get_path.get
dir = createDir


class GetData:   
     
    def __init__(self, data, syms):   
        print("Getting datas...")
        dir(pth('prep'))
        self.get_data(syms, data)


    def get_data(self, data, syms):
        syms = self.get_syms(syms)
        amzn = self.get_amzn(data)
        size = len(syms)      
        for i, sym in enumerate(syms):
            tmp = self.sym_data(data, sym)
            self.save_data(amzn, tmp, size, i, sym)
        print("Datas got!")
            
    
    def get_syms(self, syms):
        return [s for sym in syms for s in sym]
    
    
    def get_amzn(self, data):
        return len(self.sym_data(data, 'AMZN'))
    
    
    def sym_data(self, data, sym):
        return data[data['symbol'] == sym]
    
    
    def save_data(self, amzn, tmp, sym, i, size):    
            if len(tmp) == len(amzn): 
                print(f"{i+1}/{size}: {sym} saved!") 
                self.save_tmp(tmp, sym)
            else: 
                print(f"{i+1}/{size}: {sym} failed!")
    
    
    def save_tmp(self, tmp, sym):
        tmp = tmp.set_index('data').drop(columns=['symbol'])
        tmp.to_csv(os.path.join(pth('prep'), f'{sym}.csv'))