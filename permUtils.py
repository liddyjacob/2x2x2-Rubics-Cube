def element_in(element, cycles):
  for cycle in cycles:
    if element in set(cycle):
      return True;

  return False;

def permute(element, cycles):

  new_cycle = (element,)

  while True:

    #Set the current element to the end of the cycle:
    path_element = new_cycle[-1]

    #The element has not been permuted yet.
    mutated = False

    for cycle in reversed(cycles):
      if path_element in cycle:

        #The element is permutated.
        mutated = True

        #Find what the element goes to:
        index = cycle.index(path_element)
        path_element = cycle[(index + 1) % len(cycle)]
  
    #The case where we return to the first element after all cycles.
    if path_element == element:
      break
    
    if path_element == new_cycle[-1]:
      break

    if not mutated:
      break

    # Add the next element to the cycle if it has not broken any 
    # of the conditions.
    new_cycle += (path_element,)
    

  return new_cycle      

def disjoint(cycles):
  
  collected_elements = {}

  for cycle in cycles:
    for element in cycles:
      #Not disjoint if an element is repeated.
      if element in collected_elements:
        return False
      


def simplify(cycles):
  
  new_cycles = []

  # No cycles : Nothing to do.
  if len(cycles) == 0:
    return new_cycles

  # Disjoint cycles: Nothing to do.
  if disjoint(cycles):
    return cycles

  for cycle_index in reversed(range(len(cycles))):
    cycle = cycles[cycle_index]
    #1-cycles are uninteresting
    if len(cycle) == 1:
      continue

    for element_index in range(0,len(cycle)):
      
      element = cycle[element_index]

      if not element_in(element, new_cycles):
        new_cycle = permute(element, cycles)
        if len(new_cycle) != 1:
          new_cycles.append(new_cycle);


  return new_cycles

 
