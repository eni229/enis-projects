package main;

import java.awt.Graphics;

import entities.Player;

public class Game2D implements Runnable{
	
	private GameWindow gameWindow;
	private GamePanel gamePanel;
	private Thread gameThread;
	private final int FPS_SET = 120;
	private final int UPS_SET = 200;	
	private Player player;
	private levels.levelManager levelManager;
	
	public final static int defaultTileSize = 32;
	public final static float scale = 1.0f;
	public final static int tileWidth = 26;
	public final static int tileHeight = 14;
	public final static int tilesSize = (int) (defaultTileSize * scale);
	public final static int gameWidth = tilesSize * tileWidth;
	public final static int gameHeight = tilesSize * tileHeight;

	public Game2D() {
		
		initClasses();
		gamePanel = new GamePanel(this);
		gameWindow = new GameWindow(gamePanel);
		gamePanel.setFocusable(true);
		gamePanel.requestFocus(); 
		
		startGameLoop();
		
	}
	
	private void initClasses() {
		player = new Player(200, 200);
		levelManager = new levels.levelManager(this);
	}

	private void startGameLoop() {
		gameThread = new Thread(this);
		gameThread.start();
	}
	public void update() {
		levelManager.update();
		player.update();
	}
	
	public void render(Graphics g) {
		levelManager.draw(g);
		player.render(g);

	}

	@Override
	public void run() {
		
		double timePerFrame = 1000000000.0 / FPS_SET;
		double timePerUpdate = 1000000000.0 / UPS_SET;
		
		long previousTime = System.nanoTime();
		
		int frames = 0;
		int updates = 0;
		long lastCheck = System.currentTimeMillis();
		
		double changeu = 0; 
		double changef = 0;
		
		while (true) {
			long currentTime = System.nanoTime();
			
			changeu += (currentTime - previousTime) / timePerUpdate;
			changef += (currentTime - previousTime) / timePerFrame;
			previousTime = currentTime;
			
			if (changeu >=1) {
				update();
				updates++;
				changeu--;
			}
			
			if (changef >=1) {
				gamePanel.repaint();
				frames++;
				changef--;
			}
				
			if (System.currentTimeMillis() - lastCheck >= 1000) {
				lastCheck = System.currentTimeMillis();
				System.out.println("FPS: " + frames + "| UPS: " + updates); 
				frames = 0;
				updates = 0;
			}
			
		}
		
	}
	public void windowFocusLost() {
		player.resetDirBooleans();
	}
	public Player getPlayer() {
		return player; 
	}

}
