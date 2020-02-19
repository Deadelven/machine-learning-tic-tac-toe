import keras
import h5py
import glob
import numpy
from keras.models import Sequential
from keras.layers import Dense
model =""


def createModel():
	model = Sequential()
	model.add(Dense(11, input_dim=1))
	model.add(Dense(64))
	model.add(Dense(128))
	model.add(Dense(256))
	model.add(Dense(18))
	model.add(Dense(9))
	return model
	
def pred(model,game):
	print("game")
#	print(model.predict((game[0],game[1],game[2],game[3],game[4],game[5],game[6],game[7],game[8])))
	return model.predict(game)

#game =[1,-1,0,0,0,0,0,0,0,0.2]
#createModel()
#print(pred(model,game)[0])
