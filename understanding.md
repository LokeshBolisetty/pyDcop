# pydcop

## utils
### dcop_cli.py
This is similar to git. When you do ```git commit```, git is the cli and commit is the command. Similarly, here pydcop is the cli and the arguments follow it. 
```
dcop_cli.py agent ... 
pydcop agent ...
```
are identicaly
The arguments are specific to each command. Some arguments like verbosity are common to all command, they are called global arguments. 
The global arguments avaiable are
```
pydcop [--version] [--timeout <timeout>] [--verbosity <level>]
       [--log <log_conf_file>]

```
Verbosity can take 0,1,2,3 where 0 implies print only errors and the output is yaml fomatted result of the command. Default value is 0. 

Additionally --help/-h can always be used as both global and local argument. 
## Graphs
There are three types of graphs in PyDCOP. They are
1. Factor graph
2. Pseudo Graph
3. Constraints hypergraph

The codes for these graphs are in graphs


## dcop
### dcop.py
All the attributes we need to set for a problem can be given directly to dcop. 

A dcop is uniquely identified by 
1. Variables
2. Domains
3. Constraints
4. Agents

In the dcop file, we can give all these along with others like objective and algorithms.
All these values can be set in a .yaml file and be loaded into dcop. 

### objects.py
It has many classes which will be used to build the dcop. 

The classes include
1. Domain
2. Variable
3. BinaryVariable
4. VariableWithCostDict
5. VariableWithCostFunc
6. VariableNoisyCostFunc
7. ExternalVariable
8. AgentDef

The AgentDef object is very crucial as the agents are made using it.

### scenario.py

Action -> Something like an agent disappearing
Event -> Several actions happening at the same time
Scenario -> List of events in a system. 

### yamldcop.py
Responsible for loading a file or more files into the dcop. 

## Commands
All the commands that one can run using PyDCOP have their code in this folder.

Every file in this folder has 
1. A ```set_parser``` function which parses the arguments
2. A ```run_cmd``` function which acts like the main function for the command we are trying to run
3. An ```on_timeout``` function which determines what to do when the set timelimit has been exceeded
4. An ```on_force_exit``` function which determines what to do when the user presses Ctrl+C

### untils.py
Is a utility file which facilitates the creation of csv file to store the metrics etc.

### agent.py
Runs one or more standalone agents. 
```
pydcop agent --names <names>
            [--address <ip_address>] 
            [--port <start_port>]
            --orchestrator <ip[:<port>]>
            [--uiport <start_uiport>]
            [--restart]
            [--delay <delay>]
```
Orchestrator will not be started along with these agents. You need to run them seperately. 

### orchestrator.py
This is the orchestrator for our application. When the orchestrator stops, so do all other agents. This is the file in which we have the code corresponding to the computation graph type etc. 

```
pydcop orchestrator --algo <algo> 
                    [--algo_params <params>]
                    --distribution <distribution>
                    [--address <ip_addr>] 
                    [--port <port>]
                    [--uiport <uiport>]
                    [--collect_on <collect_mode>] 
                    [--period <p>]
                    [--run_metrics <file>]
                    [--end_metrics <file>]
                    <dcop_files>
```
algo specifies which algorithm to take eg: MGM DPOP etc

algo_params are the optional paramters that can be sent to the algorithm. They are sent as "name:value" string

distribution selects the distribution required. By default it takes oneagent. 

collect_on : When do you collect the metric? cycle_change or value_change or period

period : You can collect on a time by giving --period p where p is in seconds. Note that this can be used only when collect_on is set to period.

### graph.py 
Has the code corresponding to the graphs. 
```
pydcop graph --graph <graph_model> <dcop_files>
```
graph allows you to set the graph_mode out of factor_graph, pseudotree and constraints_hypergraph.

display helps you see the graph using matplotlib. 

dcop_files allow you to write the dcop in a graph and use it. If you give multiple paths here, they will be concatenated to one .yaml file and used. 

### generate.py
It creates random graphs for us to use. It has different use cases like iot, meetingscheduling, ising etc. 
```
 pydcop generate [--output <file>] <problem-type> ...
```
The command depends on the use case we are trying to generate. So use ```pydcop generate problem-type --help``` to understand how to use the command. 
```
pydcop generate --c meetings 
                --slots_count  10 
                --events_count 5 
                --resources_count 15 
                --max_resources_event 14 
                --max_length_event 12 
                --no_agents
``` 
will generate the details required for a random meeting event.

### batch.py

Batching allows you to run different commands at once. The commands have to be put in a file and used. 
```
pydcop batch <batches_description_file>
```
### solve.py
This allows you to run static dcop algorithms. 
```
  pydcop solve --algo <algo> [--algo_params <params>]
               [--distribution <distribution>]
               [--mode <mode>]
               [--collect_on <collect_mode>]
               [--period <p>]
               [--run_metrics <file>]
               [--end_metrics <file>]
               [--delay <delay>]
               [--uiport <port>]
               <dcop_files>
```
This is a shorthand for ```agent``` and ```orchestrator```. 

### run.py
This is the same as solve.py except you can run dynamic dcop algorithms here. 
```
pydcop run --algo <algo> [--algo_params <params>]
               [--distribution <distribution>]
               [--replication_method <replication method>]
               [--ktarget <resiliency_level>]
               [--mode <mode>]
               [--collect_on <collect_mode>]
               [--period <p>]
               [--run_metrics <file>]
               [--end_metrics <file>]
               --scenario <scenario_file>
               <dcop_files>
```

## To add a new field in the variables
1. Add property to the Variable class in object.py and to others like ExternalVariables if required
2. Add the fields in _build_variables in yamldcop.py
3. Add mapping in NAryFunctionRelation in relations.py. Inside NAryFunctionRelation, in get_value_for_instace, add the values for the newly added properties also. 
4. Supass the "Missing Variable" check in constraint_from_str function in relations.py
