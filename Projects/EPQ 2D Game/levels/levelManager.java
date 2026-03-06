package levels;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;

import main.Game2D;
import utilise.loadsave;

public class levelManager {
	
	private Game2D game2D;
	private BufferedImage grassbg = loadsave.getSprite(loadsave.grassbgData);
	private BufferedImage[] grassSprite;
	private Level level;
	private BufferedImage wallSprite;
	private BufferedImage stoneGroundSprite;
	private BufferedImage shadowSprite;
	

	public levelManager(Game2D game2D) {
		this.game2D = game2D;
	}
	
	public void draw(Graphics g ) {		
		g.drawImage(grassbg, 0, 0, 64* Game2D.tilesSize, 64 * Game2D.tilesSize, null);
		
	}
	public void update() {
		
	}
}
