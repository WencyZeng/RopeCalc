import math

def calculate_rope_weight(weight, angle):
    # Convert angle to radians
    angle_rad = math.radians(90 -angle/2)
    
    # Calculate the tension in each rope
    tension_per_rope = (weight / 2) / math.sin(angle_rad)
    
    return tension_per_rope

# Given values
person_weight = 95  # kg
angle_between_ropes = 45  # degrees

# Calculate the weight (tension) in each rope
rope_weight = calculate_rope_weight(person_weight, angle_between_ropes)

print(f"The weight (tension) in each rope: {rope_weight:.2f} kg")

import matplotlib.pyplot as plt
import numpy as np

def draw_diagram(weight, angle, tension):
    # Create a new figure
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Calculate components
    angle_rad = math.radians(90-angle / 2)
    dx = tension * math.cos(angle_rad)
    dy = tension * math.sin(angle_rad)
    
    # Draw ropes
    ax.arrow(0, 0, dx, dy, head_width=2, head_length=4, fc='r', ec='r', width=0.5)
    ax.arrow(0, 0, -dx, dy, head_width=2, head_length=4, fc='r', ec='r', width=0.5)
    
    # Draw weight
    ax.arrow(0, 0, 0, -weight, head_width=2, head_length=4, fc='b', ec='b', width=0.5)
    
    # Set limits and labels
    ax.set_xlim(-tension-5, tension+5)
    ax.set_ylim(-weight-5, dy+5)
    ax.set_aspect('equal')
    
    # Add labels
    ax.text(dx+1, dy/2, f'T = {tension:.2f} kg', color='r')
    ax.text(-dx-15, dy/2, f'T = {tension:.2f} kg', color='r')
    ax.text(2, -weight/2, f'W = {weight:.2f} kg', color='b')
    ax.text(0, dy+2, f'Angle = {angle}°', ha='center')
    
    # Set title
    ax.set_title('Rope Tension Diagram')
    
    # Remove axis
    ax.axis('off')
    
    plt.show()

# Draw the diagram
draw_diagram(person_weight, angle_between_ropes, rope_weight)

import streamlit as st
import math
import matplotlib.pyplot as plt

def calculate_rope_weight(weight, angle):
    angle_rad = math.radians(angle)
    return weight / (2 * math.cos(angle_rad / 2))

st.title('Rope Tension Calculator and Diagram')

person_weight = st.number_input('Person Weight (kg)', min_value=1.0, max_value=500.0, value=95.0, step=0.1)
angle_between_ropes = st.number_input('Angle Between Ropes (degrees)', min_value=1.0, max_value=179.0, value=45.0, step=0.1)

if st.button('Calculate and Draw Diagram'):
    st.sidebar.markdown("**Author:** Wency Zeng")
    rope_weight = calculate_rope_weight(person_weight, angle_between_ropes)
    
    st.write(f"The weight (tension) in each rope: {rope_weight:.2f} kg")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    angle_rad = math.radians(90-angle_between_ropes / 2)
    dx = rope_weight * math.cos(angle_rad)
    dy = rope_weight * math.sin(angle_rad)
    
    ax.arrow(0, 0, dx, dy, head_width=2, head_length=4, fc='r', ec='r', width=0.5)
    ax.arrow(0, 0, -dx, dy, head_width=2, head_length=4, fc='r', ec='r', width=0.5)
    ax.arrow(0, 0, 0, -person_weight, head_width=2, head_length=4, fc='b', ec='b', width=0.5)
    
    ax.set_xlim(-rope_weight-5, rope_weight+5)
    ax.set_ylim(-person_weight-5, dy+5)
    ax.set_aspect('equal')
    
    ax.text(dx+1, dy/2, f'T = {rope_weight:.2f} kg', color='r')
    ax.text(-dx-15, dy/2, f'T = {rope_weight:.2f} kg', color='r')
    ax.text(2, -person_weight/2, f'W = {person_weight:.2f} kg', color='b')
    ax.text(0, dy+2, f'Angle = {angle_between_ropes}°', ha='center')
    
    ax.set_title('Rope Tension Diagram')
    ax.axis('off')
    
    st.pyplot(fig)



