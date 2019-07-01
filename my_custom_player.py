
from sample_players import DataPlayer


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state - calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques (minimax search with alpha-beta pruning 
        #       and iterative deepening) from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        #self.queue.put(random.choice(state.actions()))
        #print(state.ply_count)
        best_move = None
        #for depth in range(1, depth_limit+1):
        #    best_move = minimax_decision(gameState, depth)
        #return best_move
        #action = self.mcts()
        #self.queue.put(action)
        #self.context = object_you_want_to_save  # self.context will contain this object on the next turn
        
        if state.ply_count < 4:
            self.queue.put(random.choice(state.actions()))
        else:
            ###### iterative deepening ######
            depth_limit = 4
            for depth in range(1, depth_limit + 1):
                #best_move = alpha_beta_search(state, self.player_id,depth)
                best_move = alpha_beta_search(state, depth)
            self.queue.put(best_move)
            
    #def alpha_beta_search("""self, """state, depth):
    def alpha_beta_search(state, depth):
        """ Return the move along a branch of the game tree that
        has the best possible value.  A move is a pair of coordinates
        in (column, row) order corresponding to a legal move for
        the searching player.
        
        You can ignore the special case of calling this function
        from a terminal state.
        """
        player_id = state.player()
        
        alpha = float("-inf")
        beta = float("inf")
        best_score = float("-inf")
        best_move = None
        for a in gameState.actions():
            v = min_value(gameState.result(a), alpha, beta)
            alpha = max(alpha, v)
            if v > best_score:
                best_score = v
                best_move = a
        return best_move

    # TODO: modify the function signature to accept an alpha and beta parameter
    def min_value(gameState, alpha, beta):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        if gameState.terminal_test():
            return gameState.utility(0)
        
        v = float("inf")
        for a in gameState.actions():
            # TODO: modify the call to max_value()
            v = min(v, max_value(gameState.result(a), alpha, beta))
            # TODO: update the value bound
            if v <= alpha:
                return v
            beta = min(beta,v)
        return v
    
    # TODO: modify the function signature to accept an alpha and beta parameter
    def max_value(gameState, alpha, beta):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        if gameState.terminal_test():
            return gameState.utility(0)
        
        v = float("-inf")
        for a in gameState.actions():
            # TODO: modify the call to min_value()
            v = max(v, min_value(gameState.result(a), alpha, beta))
            # TODO: update the value bound
            if v >= beta:
                return v
            alpha = max(alpha,v)
        return v
        
    def utility(self, state):
        my_loc = state.locs[self.player_id]
        my_liberties = state.liberties(own_loc)
        return len(my_liberties)
    
#        player_loc = state.locs[self.player_id]
#        player_liberties = state.liberties(player_loc)
#        opponent_loc = state.locs[1- self.player_id]
#        opponent_liberties = state.liberties(opponent_loc)
#        return len(player_liberties) - len(opponent_liberties)
