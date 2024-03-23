import pygame
import sys
import math
import random

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
largeur, hauteur = 800, 600
taille_fenetre = (largeur, hauteur)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Cercle blanc sur fond noir")

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Fonction pour dessiner les yeux
def draw_eyes(position_cercle):
    # Calcul de la taille du cercle en fonction du temps écoulé (fonction sinusoïdale)
    amplitude = 2  # Amplitude de variation de la taille du cercle
    periode = 2000  # Période de la fonction sinusoïdale en millisecondes
    temps_ecoule = pygame.time.get_ticks() - temps_debut
    rayon = amplitude * math.sin(2 * math.pi * temps_ecoule / periode) + 30  # Variation de la taille du cercle

    # Dessiner le cercle blanc
    pygame.draw.circle(fenetre, BLANC, position_cercle, int(rayon))
    # Dessiner le cercle noir à l'intérieur pour les yeux
    pygame.draw.circle(fenetre, NOIR, position_cercle, (int(rayon) - 10))

# Fonction pour calculer la progression du mouvement
def move_object(start_pos, target_pos, duration, elapsed_time):
    elapsed_time = min(elapsed_time, duration)
    progress = elapsed_time / duration
    # Calculer la position actuelle en fonction de la progression du mouvement
    current_pos = (
        start_pos[0] + (target_pos[0] - start_pos[0]) * progress,
        start_pos[1] + (target_pos[1] - start_pos[1]) * progress
    )
    return current_pos

def curiosity(start_pos, target_pos, duration):
    # Obtenir le temps écoulé depuis le début du mouvement
    temps_ecoule = pygame.time.get_ticks() - temps_debut
    # Accéder aux positions de départ des deux cercles
    current_pos_left = move_object(start_pos["left"], target_pos, duration, temps_ecoule)
    current_pos_right = move_object(start_pos["right"], (target_pos[0]-160, target_pos[1]), duration, temps_ecoule)
    return current_pos_left, current_pos_right, temps_ecoule

clock = pygame.time.Clock()

# Boucle principale
temps_debut = pygame.time.get_ticks()
duration = 9000 
start_pos = {"left": ((largeur // 2) + 80, (hauteur // 2) - 70), "right": ((largeur // 2) - 80, (hauteur // 2) - 70)}
target_pos = (random.randint(-40, largeur-40), random.randint(-40, hauteur-80))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtenir les positions actuelles des cercles et le temps écoulé
    current_pos_left, current_pos_right, temps_ecoule = curiosity(start_pos, target_pos, duration)

    # Si le mouvement est terminé, générer une nouvelle position aléatoire pour les deux cercles
    if temps_ecoule >= duration:
        start_pos = {"left": target_pos, "right": (target_pos[0] - 160, target_pos[1])}
        target_pos = (random.randint(0, largeur), random.randint(0, hauteur))
        temps_debut = pygame.time.get_ticks()

    fenetre.fill(NOIR)

    # Dessiner les cercles
    draw_eyes(current_pos_left)
    draw_eyes(current_pos_right)

    # Mettre à jour l'affichage
    pygame.display.flip()
    pygame.time.Clock().tick(60)
