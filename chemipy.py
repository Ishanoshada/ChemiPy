# Function to format electron configuration to use superscripts
def format_electron_configuration(config):
    # Replace electron counts like 1s2 with proper superscript notation
    config = config.replace('1s2', '1s²').replace('2s2', '2s²').replace('2p6', '2p⁶').replace('3s2', '3s²').replace('3p6', '3p⁶').replace('4s2', '4s²').replace('3d10', '3d¹⁰').replace('4p6', '4p⁶').replace('4d10', '4d¹⁰').replace('5s2', '5s²').replace('5p6', '5p⁶').replace('4f14', '4f¹⁴').replace('5d10', '5d¹⁰').replace('6s2', '6s²').replace('5f14', '5f¹⁴').replace('6d10', '6d¹⁰').replace('7s2', '7s²').replace('7p6', '7p⁶').replace('6p6', '6p⁶')
    # Handle single electrons, like 1s1
    config = config.replace('1s1', '1s¹').replace('2s1', '2s¹').replace('2p1', '2p¹').replace('3s1', '3s¹').replace('3p1', '3p¹').replace('4s1', '4s¹').replace('3d1', '3d¹').replace('4p1', '4p¹').replace('4d1', '4d¹').replace('5s1', '5s¹').replace('5p1', '5p¹').replace('4f1', '4f¹').replace('5d1', '5d¹').replace('6s1', '6s¹').replace('5f1', '5f¹').replace('6d1', '6d¹').replace('7s1', '7s¹').replace('7p1', '7p¹').replace('6p1', '6p¹')
    return config

# Function to generate the stable electron configuration of an atom
def electron_configuration_stable(atomic_number):
    # List of electron sublevels
    sublevels = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '4d', '5s', '5p', '4f', '5d', '6s', '5f', '6d', '7s', '7p', '6p']
    # Electron counts for each sublevel
    sublevel_electrons = {'s': 2, 'p': 6, 'd': 10, 'f': 14}
    
    electrons_left = atomic_number
    config = {}
    
    for sublevel in sublevels:
        n = int(sublevel[0])  # Principal quantum number
        l = sublevel[1]  # Angular momentum quantum number
        
        if electrons_left == 0:
            break
        
        if electrons_left >= sublevel_electrons[l]:
            electrons = sublevel_electrons[l]
        else:
            electrons = electrons_left
        
        config[sublevel] = electrons
        electrons_left -= electrons
    
    # Handle exceptions for certain elements
    exceptions = {
        24: {'4s': 1, '3d': 5},  # Chromium (Cr)
        29: {'4s': 1, '3d': 10},  # Copper (Cu)
        30: {'4s': 2, '3d': 10},  # Zinc (Zn)
        47: {'5s': 1, '4d': 10},  # Silver (Ag)
        48: {'5s': 2, '4d': 10},  # Cadmium (Cd)
        78: {'6s': 1, '4f': 14, '5d': 10},  # Platinum (Pt)
        79: {'6s': 1, '4f': 14, '5d': 10, '6p': 1},  # Gold (Au)
        80: {'6s': 2, '4f': 14, '5d': 10},  # Mercury (Hg)
        89: {'7s': 1, '5f': 14, '6d': 10},  # Actinium (Ac)
        90: {'7s': 2, '5f': 14, '6d': 10},  # Thorium (Th)
        91: {'7s': 2, '5f': 14, '6d': 10, '7p': 1},  # Protactinium (Pa)
        92: {'7s': 2, '5f': 14, '6d': 10, '7p': 2},  # Uranium (U)
        93: {'7s': 2, '5f': 14, '6d': 10, '7p': 3},  # Neptunium (Np)
        94: {'7s': 2, '5f': 14, '6d': 10, '7p': 4},  # Plutonium (Pu)
        95: {'7s': 2, '5f': 14, '6d': 10, '7p': 5},  # Americium (Am)
        96: {'7s': 2, '5f': 14, '6d': 10, '7p': 6},  # Curium (Cm)
        97: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 1},  # Berkelium (Bk)
        98: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 2},  # Californium (Cf)
        99: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 3},  # Einsteinium (Es)
        100: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 4},  # Fermium (Fm)
        101: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 5},  # Mendelevium (Md)
        102: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 6},  # Nobelium (No)
        103: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 6, '7p': 1},  # Lawrencium (Lr)
        104: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 6, '7p': 2},  # Rutherfordium (Rf)
        105: {'7s': 2, '5f': 14, '6d': 10, '7p': 6, '7p': 6, '7p': 3},  # Dubnium (Db)
        # Add more exceptions here as needed
    }
    
    if atomic_number in exceptions:
        config.update(exceptions[atomic_number])
    
    # Sort configurations by principal quantum number and sub-level energy
    ordered_config = ' '.join([f'{k}{v}' for k, v in sorted(config.items(), key=lambda x: (int(x[0][0]), sublevels.index(x[0])))])

    # Format the configuration with superscripts
    ordered_config = format_electron_configuration(ordered_config)
    return ordered_config.strip()

# Example usage:
# atomic_number = 102
# config = electron_configuration_stable(atomic_number)
# print(f'Stable Electron configuration for atomic number {atomic_number}: {config}')
