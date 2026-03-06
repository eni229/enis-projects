package utilise;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.InputStream;

import javax.imageio.ImageIO;

import main.Game2D;

public class loadsave {
	
	public static final String PlayerSprite = "character_sprites.png";
	public static final String grassSprite = "TX Tileset Grass.png";
	public static final String wallSprite = "TX Tileset Wall.png";
	public static final String stoneGroundSprite = "TX Tileset Stone Ground.png";
	public static final String shadowsSprite = "TX Shadow.png";
	public static final String grassbgData = "grass bg.png";
	
	public static BufferedImage getSprite(String Filename) {
		BufferedImage img = null;
		InputStream is = loadsave.class.getResourceAsStream("/" + Filename);
		
		try {
		img = ImageIO.read(is);
		
		} catch(IOException e) {
			e.printStackTrace();
		}finally {
			try {
				is.close();
			}catch (IOException e){
				e.printStackTrace();
			}
		}
		return img;
	}
//	public static int[][] getLevelData(){
//		int[][] levelData = new int[Game2D.tileHeight][Game2D.tileWidth];
//		BufferedImage img = getSprite(grassbgData);
//		
//		for (int j = 0; j < img.getHeight(); j++) {
//			for (int i = 0; i < img.getWidth(); i++) {
//				Color color = new Color(img.getRGB(i, j));
//				int value = color.getRed();
//				if (value >= 64) {
//					value = 0;
//					levelData[j][i] = value;
//				}
//				
//				
//			}
//		}
//		return levelData;
//		
//	}
	
	
}
