import pandas as pd


class class_4():
    def __init__ (self,_path):
        self.df = pd.read_csv(_path)
    
    def change(self, _column):
        # 공백제거
        self.df[_column] = self.df[_column].str.replace(" ","")
        # 대문자로 변환
        self.df[_column] = self.df[_column].str.upper()
        return self.df

    def change_time(self,_column,_format = ""):
        if _format == "":
            self.df[_column] = pd.to_datetime(self.df[_column])
        else:
            self.df[_column] = pd.to_datetime(self.df[_column],format = _format)
        return self.df
    
    def ch(self, _column):
         self.df["Year"] = self.df[_column].dt.year#strftime("%Y")
         self.df["Month"] = self.df[_column].dt.month#strftime("%m")  # 한번에 뽑을때는 strftime
         self.df["Day"] = self.df[_column].dt.day#strftime("%d")
         return self.df
        
        #self.df["Year"] = self.df["purchase_date"].dt.strftime("%Y")
        #self.df["Month"] = self.df["purchase_date"].dt.strftime("%m")
        #self.df["Day"] = self.df["purchase_date"].dt.strftime("%d")

    def review(self):
        return self.df