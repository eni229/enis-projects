package utilise;



public class Constants {
	
	public static class directions{
		public static final int left = 4;
		public static final int up = 2;
		public static final int down = 1;
		public static final int right= 3;
	}
	
	public static class playerConstant {
		
		public static final int IDLE = 0;
		public static final int runningdown = 1;
		public static final int runningup = 2;
		public static final int runningright = 3;
		public static final int runningleft = 4;
		public static final int kick_attack = 5;
		public static final int punch_attack = 6;

		 
		public static int getSpriteAmount(int player_action) {
			 	
			 switch(player_action) {
			 case runningleft:
			 case runningright:
			 case runningup:
			 case runningdown:
				 return 6;
			 case IDLE:
			 case kick_attack:
			 case punch_attack:
				 return 4;
			 default:
			 return 1;
			 }
		 }
		 
	}

}
