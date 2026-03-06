package entities;

import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.InputStream;

import javax.imageio.ImageIO;

import main.Game2D;
import utilise.Constants.directions;
import utilise.Constants.playerConstant;
import utilise.loadsave;

public class Player extends entity {
	
	
	
	private BufferedImage[][] animations;
	private int aniTick, aniIndex, aniSpeed = 25;
	private int playerAction = playerConstant.IDLE;
	private int IdleDir = 0;
	public boolean moving = false, attacking = false;
	private boolean left, right, up, down;
	private float playerSpeed = 1.0f;
	
	public Player(float x, float y) {
		super(x, y);
		loadAnimations();
	}
	
	public void update() {
		
		updatePos();
		updateAnimationTick();
		setAnimation();
		
	}
	
	public void render(Graphics g) {
		
		if (moving == true) {
				g.drawImage(animations[playerAction][aniIndex], (int)x, (int)y,  128 * (int)Game2D.scale,  128 * (int)Game2D.scale, null);
			}
		
		else {
			g.drawImage(animations[playerAction][IdleDir], (int)x, (int)y, 128 * (int)Game2D.scale, 128* (int) Game2D.scale, null);
		}
		
		
		
	
		
		
	
	}
	

	
	public void updateAnimationTick() {
		aniTick++;
		if(aniTick >= aniSpeed) {
			aniTick = 0;
			aniIndex++;
			if(aniIndex >= playerConstant.getSpriteAmount(playerAction)) {
				aniIndex = 0;
				attacking = false;
				} 
			}
	
		
		
	}
	
	public void setAnimation() {
		
		int startAni = playerAction;
	
	
		if (moving == true) {
			if (left == true) {
				playerAction = playerConstant.runningleft;
				IdleDir = 3;
			}
			else if (right == true) {
				playerAction = playerConstant.runningright;
				IdleDir = 2;
			}
			else if (up == true) {
				playerAction = playerConstant.runningup;
				IdleDir = 1;
			}
			else if (down == true) {
				playerAction = playerConstant.runningdown;
				IdleDir = 0;
			}
		}
		else if (moving == false) {
			playerAction = playerConstant.IDLE;
			
		}
		
		if(attacking == true) {
			playerAction = playerConstant.kick_attack;
		}
		if(startAni != playerAction) {
			 resetAniTick();
		}
		
	}
	public void resetAniTick() {
		aniTick = 0;
		aniIndex = 0;
	}
	
	public void updatePos() {
		
		moving = false;
		
		if (left && !right) {
			x -= playerSpeed; 
			moving = true;
		}
		else if (right && !left) {
			x += playerSpeed;
			moving = true;
		}
		
		if (up && !down) {
			y -= playerSpeed;
			moving = true;
		}
		else if(down && !up){
			y += playerSpeed;
			moving = true;
		}
		

	}
	
	private void loadAnimations() {
		
		InputStream is = getClass().getResourceAsStream("/character_sprites.png");

		BufferedImage img = loadsave.getSprite(loadsave.PlayerSprite);
		
		animations = new BufferedImage[7][6];
		for (int j = 0; j < animations.length; j++) {
			for (int i = 0; i < animations[j].length; i++) {
				animations[j][i] = img.getSubimage(i*64,j*64, 64, 64);
			}
		}
			
	}
	
	public void resetDirBooleans() {
		left = false;
		right = false;
		up = false;
		down = false;
	}
	public void setAttack(boolean attacking) {
		this.attacking = attacking;
	}
	
	public boolean isLeft() {
		return left;
	}

	public void setLeft(boolean left) {
		this.left = left;
	}

	public boolean isRight() {
		return right;
	}

	public void setRight(boolean right) {
		this.right = right;
	}

	public boolean isUp() {
		return up;
	}

	public void setUp(boolean up) {
		this.up = up;
	}

	public boolean isDown() {
		return down;
	}

	public void setDown(boolean down) {
		this.down = down;
	}
		
	

}
	

