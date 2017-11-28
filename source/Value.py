data_path="../data/"
subjects_filename=data_path+"subjects.csv"
groups_filename=data_path+"groups.csv"
teachers_filename=data_path+"sub_teachers.csv"
rooms_filename=data_path+"allot_room.csv"
labs_filename=data_path+"allot_lab.csv"
classes_filename=data_path+"classes.csv"

max_pop=16
no_of_groups=9

working_days=5
working_hours=11
lec_slot_prob=[0.20,0.20,0.20,0.20,0.03,0.00,0.05,0.05,0.05,0.01,0.01]
tut_slot_prob=[0.01,0.01,0.01,0.01,0.01,0.00,0.31,0.31,0.31,0.01,0.01]
prac_slot_prob=[0.02,0.02,0.02,0.02,0.00,0.00,0.30,0.30,0.30,0.01,0.01]

crossover_points=5

population_mutation_prob=0.7
offspring_mutation_prob=0.2
max_trials_for_free_slots=10

unfit_mutation_size=5
fit_mutation_size=1