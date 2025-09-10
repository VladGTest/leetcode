class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
       int m = languages.length;
        
        Set<Integer>[] userLanguages = new Set[m + 1];
        for (int i = 0; i <= m; i++) {
            userLanguages[i] = new HashSet<>();
        }
        
        for (int i = 0; i < languages.length; i++) {
            int userId = i + 1;
            for (int lang : languages[i]) {
                userLanguages[userId].add(lang);
            }
        }
        
        boolean[] alreadyCommunicate = new boolean[friendships.length];
        for (int i = 0; i < friendships.length; i++) {
            int u = friendships[i][0];
            int v = friendships[i][1];
            
            for (int lang : userLanguages[u]) {
                if (userLanguages[v].contains(lang)) {
                    alreadyCommunicate[i] = true;
                    break;
                }
            }
        }
        
        Set<Integer> usersToTeach = new HashSet<>();
        
        for (int lang = 1; lang <= n; lang++) {
            Set<Integer> currentUsers = new HashSet<>();
            
            for (int i = 0; i < friendships.length; i++) {
                if (alreadyCommunicate[i]) continue;
                
                int u = friendships[i][0];
                int v = friendships[i][1];
                
                if (!userLanguages[u].contains(lang)) {
                    currentUsers.add(u);
                }
                if (!userLanguages[v].contains(lang)) {
                    currentUsers.add(v);
                }
            }
            
            if (usersToTeach.isEmpty() || currentUsers.size() < usersToTeach.size()) {
                usersToTeach = currentUsers;
            }
        }
        
        return usersToTeach.size();
}}