CREATE TABLE IF NOT EXISTS reviewer_state (
 reviewer TEXT PRIMARY KEY,
 revision INTEGER NOT NULL DEFAULT 0,
 decisions TEXT NOT NULL DEFAULT '{}',
 write_id TEXT
);
CREATE TABLE IF NOT EXISTS decision_events (
 write_id TEXT PRIMARY KEY,
 reviewer TEXT NOT NULL,
 saved_at TEXT NOT NULL,
 revision INTEGER NOT NULL,
 changes TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS screening_decisions (
 reviewer TEXT NOT NULL,
 record_id TEXT NOT NULL,
 value TEXT NOT NULL,
 PRIMARY KEY (reviewer, record_id)
);
