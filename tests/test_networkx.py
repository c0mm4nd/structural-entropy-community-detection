import unittest
import networkx as nx
from se_community import community_detection


class TestNetworkX(unittest.TestCase):

    def test_karate_club(self):
        G = nx.karate_club_graph()
        communities = community_detection(G, verbose=True)
        # should have 2 communities
        community_count = len(set(communities.values()))
        print("got", community_count, "communities")
        self.assertTrue(community_count >= 2)
        print(communities)


    # def test_gn_graph(self):
    #     G = nx.gn_graph(100)
    #     communities = community_detection(G, size_threshold=3, max_depth=3)
    #     # should have 2 communities
    #     community_count = len(set(communities.values()))
    #     self.assertEqual(community_count, 2)
    #     print(communities)

    def test_stochastic_block_model(self):
        sizes = [50, 50, 50, 50]  # community sizes
        p_in = 0.9  # probability of an edge within a community
        p_out = 0.01  # probability of an edge between communities
        G = nx.stochastic_block_model(
            sizes,
            [
                [p_in, p_out, p_out, p_out],
                [p_out, p_in, p_out, p_out],
                [p_out, p_out, p_in, p_out],
                [p_out, p_out, p_out, p_in],
            ],
        )
        print("graph generated", G.number_of_nodes(), G.number_of_edges())
        communities = community_detection(G, verbose=True)
        # should have 4 communities
        community_count = len(set(communities.values()))
        self.assertTrue(community_count >= 4)
        print(communities)


if __name__ == "__main__":
    unittest.main()
