CREATE TABLE IF NOT EXISTS reviewer_state (reviewer TEXT PRIMARY KEY, revision INTEGER NOT NULL DEFAULT 0, write_id TEXT);
CREATE TABLE IF NOT EXISTS practice_decisions (reviewer TEXT NOT NULL, stage TEXT NOT NULL, record_id TEXT NOT NULL, value TEXT NOT NULL, PRIMARY KEY(reviewer,stage,record_id));
CREATE TABLE IF NOT EXISTS decision_events (write_id TEXT PRIMARY KEY, reviewer TEXT NOT NULL, saved_at TEXT NOT NULL, revision INTEGER NOT NULL, changes TEXT NOT NULL);
