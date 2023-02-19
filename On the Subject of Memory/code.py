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
    1: "4",
    2: 'instr[1]["pressed"]["instruction"]',
    3: "sequence[0]",
    4: 'instr[1]["pressed"]["instruction"]',
    "pressed": {"label": None, "instruction": None},
}
instr[3] = {
    1: 'instr[2]["pressed"]["label"]',
    2: 'instr[1]["pressed"]["label"]',
    3: "sequence[2]",
    4: "4",
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
  for i in range(1, len(stages)+1):
      if len(stages[i-1]) <= 0: continue
      sequence, prompt = stages[i-1][:-1], stages[i-1][-1]
      
      # check if the instruction exists
      instruction_set = instr.get(i, False)
      if not instruction_set: continue
      instruction = instruction_set.get(prompt, False)
      if not instruction: continue
      
      try:
        label = eval(instruction)
        # keep evaluating the instruction until it converges
        while  not isinstance(label, int):
          label = eval(str(label))
        code += str(label)
      except:
         continue

      # update the instruction array
      instr[i]["pressed"]["label"] = label
      instr[i]["pressed"]["instruction"] = instruction

  if len(code) > 0:
    return int(code)
  return 0


code = decipher([[1,3,2,4,1],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,2],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,3],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,1],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,2],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,4],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,1],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,3],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,4],
 [2,1,4,3,1],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,2],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,3],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,4],
 [4,1,2,3,4]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,1]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,2]])
print(code)

code = decipher([[1,3,2,4,4],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,3]])
print(code)