#include <glut.h>

float _angle = 0.0;

void Draw() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glColor3f(0.7, 0.1, 0.3);

	glPushMatrix();
			glRotatef(_angle, 0.0, 1.0, 0.0);
			glutSolidTorus(0.2, 0.7, 9, 25); // inner radius, outer radius, sides, segments
	glPopMatrix();

	glFlush();
}

void update(int value)
{
	_angle += 0.2;
	if (_angle > 360)
	{
	_angle - 0.0;
	}

	glutPostRedisplay();
	glutTimerFunc(1,update,0);
}

void lightSettings()
{
	glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE );
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);

	GLfloat ambientLight[] = {0.2, 0.2, 0.2, 1.0};
	GLfloat diffuseLight[] = {0.8, 0.8, 0.8, 1.0};
	GLfloat specularLight[] = {1.0, 1.0, 1.0, 1.0};

	glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight);
//	glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight);

	GLfloat lightPosition[] = {-1.0, -1.0, 0.0};
	glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);

	
}

void Initialize() {
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);
	lightSettings();
}

int main(int iArgc, char** cppArgv) {
	glutInit(&iArgc, cppArgv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(250, 250);
	glutInitWindowPosition(200, 200);
	glutCreateWindow("CSE");
	Initialize();
	glutDisplayFunc(Draw);
	update(0);
	glutMainLoop();
	return 0;
}