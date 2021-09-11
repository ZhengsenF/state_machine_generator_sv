# State Machine Generator
## Files
`state_machine_gen.py`: takes two argument and generate sv file automatically  
`config_template.csv`: configuration template that you should start with  
`config_example.csv`: an example state machine provided  
`example.sv`: example state machine sv file generated from `config_example.csv`  

## Usage
### Config formate
The default case is `next_state = state;`
| STATE      | TRANSITION_LOGIC | NEXT_STATE |
| ----------- | ----------- | ----------- |
| START_STATE      | logic to next state (if)       | intended next state|
| |logic to next state (else if)  |intended next state|
|||intended next state (else)|
| STATE_1   |         | intended next state (direct transition)|
| STATE_2   |  logic to next state (single if)       | intended next state|
| STATE_3   |  logic to next state (if)       | intended next state|
|   |      | intended next state (else)|


### Run the script
The script takes two args:  
1. path of the csv configuration file
2. path of the output sv file
```
python3 state_machine_gen.py config_file.csv output.sv
```
