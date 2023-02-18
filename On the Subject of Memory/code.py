# Contains instructions on how to evaluate each rule
instr = {
    1: {
      1: "sequence[1]",
      2: "sequence[1]",
      3: "sequence[2]",
      4: "sequence[3]",
      "pressed": {"label": None, "instruction": None},
    },
}
instr[2] = {
    1: "sequence[4]",
    2: 'instr[1]["pressed"]["instruction"]',
    3: "sequence[0]",
    4: 'instr[1]["pressed"]["instruction"]',
    "pressed": {"label": None, "instruction": None},
}
instr[3] = {
    1: 'instr[2]["pressed"]["label"]',
    2: 'instr[1]["pressed"]["label"]',
    3: "sequence[2]",
    4: "sequence[4]",
    "pressed": {"label": None, "instruction": None},
}
instr[4] = {
    1: 'instr[1]["pressed"]["instruction"]',
    2: "sequence[0]",
    3: 'instr[2]["pressed"]["instruction"]',
    4: 'instr[2]["pressed"]["instruction"]',
    "pressed": {"label": None, "instruction": None},
}
instr[5] = {
    1: 'instr[1]["pressed"]["instruction"]',
    2: 'instr[2]["pressed"]["instruction"]',
    3: 'instr[3]["pressed"]["instruction"]',
    4: 'instr[4]["pressed"]["instruction"]',
    "pressed": {"label": None, "instruction": None},
}



def decipher(stages):
  code = ''
  for i in range(1, 6):
      sequence, prompt = stages[i-1][:-1], stages[i-1][-1]
      
      # get the instruction and evaluate it
      instruction = instr[i][prompt]
      label = eval(instruction)

      # keep evaluating the instruction until it converges
      while  not isinstance(label, int):
        label = eval(str(label))
      code += str(label)

      # update the instruction array
      instr[i]["pressed"]["label"] = label
      instr[i]["pressed"]["instruction"] = instruction
  return int(code)


code = decipher([[1,3,2,4,1],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])

print(code)