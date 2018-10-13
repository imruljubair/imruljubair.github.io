
#include <iostream>
#include <stdlib.h>

#include <glut.h>

#include "imageloader.h"

using namespace std;


GLuint _textureId; 
GLuint _textureId1; 



void drawScene() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	
	glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

glPushMatrix();

	glTranslatef(0.0, -1.0, -5.0f);
	
	glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, _textureId);
	

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

	glColor3f(1.0f, 1.0f, 1.0f);
	glBegin(GL_QUADS);
	
	glNormal3f(0.0f, 0.0f, 1.0f);

	glTexCoord2f(0.0, 0.0);
	glVertex3f(-1.0, -1.0, 0.0);

	glTexCoord2f(0.0, 5.0);
	glVertex3f(-1.0, 1.0, 0.0);

	glTexCoord2f(5.0, 5.0);
	glVertex3f(1.0, 1.0, 0.0);

	glTexCoord2f(5.0, 0.0);
	glVertex3f(1.0, -1.0, 0.0);
	
	glEnd();

glPopMatrix();

glPushMatrix();

	glBindTexture(GL_TEXTURE_2D, _textureId1);
	

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

	glTranslatef(0.0, 1.0, -5.0f);

	glBegin(GL_QUADS);
	
	glNormal3f(0.0f, 0.0f, 1.0f);

	glTexCoord2f(0.0, 0.0);
	glVertex3f(-1.0, -1.0, 0.0);

	glTexCoord2f(0.0, 5.0);
	glVertex3f(-1.0, 1.0, 0.0);

	glTexCoord2f(5.0, 5.0);
	glVertex3f(1.0, 1.0, 0.0);

	glTexCoord2f(5.0, 0.0);
	glVertex3f(1.0, -1.0, 0.0);
	
	glEnd();


glPopMatrix();

	glutSwapBuffers();
}

GLuint loadTexture(Image* image) {
	GLuint textureId;
	glGenTextures(1, &textureId); //Make room for our texture
	glBindTexture(GL_TEXTURE_2D, textureId); //Tell OpenGL which texture to edit
	//Map the image to the texture
	glTexImage2D(GL_TEXTURE_2D,                //Always GL_TEXTURE_2D
				 0,                            //0 for now
				 GL_RGB,                       //Format OpenGL uses for image
				 image->width, image->height,  //Width and height
				 0,                            //The border of the image
				 GL_RGB, //GL_RGB, because pixels are stored in RGB format
				 GL_UNSIGNED_BYTE, //GL_UNSIGNED_BYTE, because pixels are stored
				                   //as unsigned numbers
				 image->pixels);               //The actual pixel data
	return textureId; //Returns the id of the texture
}

void initialize() {
	
	glClearColor(1.0, 1.0, 1.0, 1.0);
	glMatrixMode(GL_PROJECTION);
	gluPerspective(45.0, 1.00, 1.0, 200.0);
	Image* image = loadBMP("F:\\aust3.bmp");
	Image* image1 = loadBMP("F:\\aust4.bmp");
	_textureId = loadTexture(image);
	_textureId1 = loadTexture(image1);
	delete image;
}

void lightSetting()
{

	GLfloat ambientIntensity[4] = {0.6, 0.6, 0.6, 1.0}; 
	
	GLfloat position[4] = {0.0, 1.0, 0.0, 0.0}; 

	glEnable(GL_DEPTH_TEST); 
	glEnable(GL_COLOR_MATERIAL); 

	glEnable(GL_LIGHTING); 
	glEnable(GL_LIGHT0); 
	glEnable(GL_NORMALIZE); 

	
	glLightfv(GL_LIGHT0, GL_AMBIENT, ambientIntensity); 
	
	glLightfv(GL_LIGHT0, GL_POSITION, position); 
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(400, 400);
	
	glutCreateWindow("Textures");
	initialize();
	lightSetting();
	glutDisplayFunc(drawScene);

	glutMainLoop();
	return 0;
}









