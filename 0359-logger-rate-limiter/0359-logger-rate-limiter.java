class Logger {
    HashMap<String, Integer> map = null;
    
    public Logger() {
        map = new HashMap<String, Integer>();
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {
        if (timestamp == 11 && message.equals("A"))
            System.out.println(map);
        if (map.containsKey(message)) {
            if (map.get(message) <= timestamp) {
                map.put(message, timestamp + 10);
                return true;
            } else
                return false;
        } else {
            map.put(message, timestamp + 10);
            return true;
        }
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */