import HMM_test

states = ('Power_Down', 'Power_Up')
symbols = ('Down', 'Up')

start_prob = {
    'Power_Down' : 0.5044,
    'Power_Up' : 0.4956
}

trans_prob = {
    'Power_Down': { 'Power_Down' : 0.262, 'Power_Up' : 0.738},
    'Power_Up': { 'Power_Down' : 0.688, 'Power_Up' : 0.312}
}

emit_prob = {
    'Power_Down': { 'Down' : 0.806, 'Up' : 0.194},
    'Power_Up': { 'Down' : 0.206, 'Up' : 0.794}
}

model = HMM_test.Model(states, symbols, start_prob, trans_prob, emit_prob)

sequence = ['Down', 'Up', 'Down']

print(model.evaluate(sequence))
print(model.decode(sequence))
