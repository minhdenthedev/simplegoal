CREATE TABLE IF NOT EXISTS goals (
    goal_id TEXT PRIMARY KEY UNIQUE NOT NULL,
    name TEXT UNIQUE NOT NULL,
    started_at TEXT NOT NULL,
    due TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS quantity_goal (
    goal_id TEXT PRIMARY KEY
        CONSTRAINT quantity_goal_fk
        REFERENCES goals(goal_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    current_quantity INTEGER NOT NULL DEFAULT 0,
    target_quantity INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS duration_goal (
    goal_id TEXT PRIMARY KEY
        CONSTRAINT quantity_goal_fk
        REFERENCES goals(goal_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    current_duration INTEGER NOT NULL DEFAULT 0,
    target_duration INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS completed_goal (
    goal_id TEXT PRIMARY KEY
        CONSTRAINT quantity_goal_fk
        REFERENCES goals(goal_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    completed_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS steps (
    step_id TEXT PRIMARY KEY UNIQUE NOT NULL,
    name TEXT NOT NULL,
    goal_id TEXT
        CONSTRAINT step_goal_fk
        REFERENCES goals(goal_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS recur_steps (
    step_id TEXT PRIMARY KEY
        CONSTRAINT recur_steps_fk
        REFERENCES steps(step_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    recur_gap INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS due_steps (
    step_id TEXT PRIMARY KEY
        CONSTRAINT due_steps_fk
        REFERENCES steps(step_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    started_at TEXT UNIQUE NOT NULL,
    due TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS completed_due_steps (
    step_id TEXT PRIMARY KEY
        CONSTRAINT completed_due_steps_fk
        REFERENCES steps(step_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    completed_at TEXT NOT NULL
);
