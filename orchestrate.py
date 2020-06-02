from environment import Room
from agent_randomaf import RandomAF
from agent_analyst import Analyst
from agent_gambler import Gambler
from agent_pintu import Pintu
import numpy as np
import matplotlib.pyplot as plt
import time


def main():

    agent = Gambler()
    room = Room()

    total_reward = 0

    iterations = 10000

    graph_step = []
    graph_score = []

    #room.room[room.state[0]][room.state[1]] = 1
    #print(room.room)

    for step in range(iterations):
        old_state = room.state
        action = agent.get_next_action(old_state)
        new_state, reward = room.take_action(action)
        agent.update(old_state, action, reward, new_state)

        total_reward += reward

        if step % 1 == 0:
            # np.append(graph_step, step)
            # np.append(graph_score, total_reward)
            graph_step.append(step)
            graph_score.append(total_reward)

        #room.room[old_state[0]][old_state[1]] = 0
        #room.room[new_state[0]][new_state[1]] = 1
        #print(room.room, end='\n')
        #print('Action:', action)
        #print('Total Reward:', total_reward)
        #print('---------------------------------------')
        #print('Q-Table:', agent.t_q_table, agent.b_q_table, agent.l_q_table, agent.r_q_table, sep='\n\n')
        #print('---------------------------------------')

        #time.sleep(1)

    print('Total Reward:', total_reward)
    #('Q-Table:', agent.t_q_table, agent.b_q_table, agent.l_q_table, agent.r_q_table, sep='\n\n'
    #print('Q-Table:', [agent.t_q_table, agent.b_q_table, agent.l_q_table, agent.r_q_table])
    #print('Q-Table:', agent.q_table)

    plt.scatter(graph_step, graph_score, 2)
    plt.show()


if __name__ == "__main__":
    main()
