int maxShared(int friends_nodes, vector<int> friends_from, vector<int> friends_to, vector<int> friends_weight) {
    int sum = 0;
    friends_weight.erase(unique(friends_weight.begin(), friends_weight.end()));
    for (int i = 0; i < friends_weight.size(); i++)
        sum += friends_weight[i];

    return sum;
}