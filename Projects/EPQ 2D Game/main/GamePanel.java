package main;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.InputStream;

import javax.imageio.ImageIO;
import javax.swing.JPanel;

import inputs.KeyboardInputs;
import inputs.MouseInputs;

import utilise.Constants.playerConstant.*;
import utilise.Constants.directions;
import utilise.Constants.directions.*;
import utilise.Constants.playerConstant;




public class GamePanel extends JPanel{

	private MouseInputs mouseInputs;
	private Game2D game2D;
	 
	public GamePanel(Game2D game2D) {
		this.game2D = game2D;
		
		mouseInputs = new MouseInputs(this); 
		
		setPanelSize();
		addKeyListener(new KeyboardInputs(this));
		addMouseListener(mouseInputs);	
		addMouseMotionListener(mouseInputs);
	}


	private void setPanelSize() {
		Dimension size = new Dimension(game2D.gameWidth, game2D.gameHeight);
		setPreferredSize(size);
	}
	
	public void updateGame() {

	}
	
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		game2D.render(g);
		
	}
	public Game2D getGame() { 
		return game2D;
	}
	}

