Feature: No Tier Jumping Policy
	Scenario Outline: Inbound L4 No Tier Jumping Rules
		Given all assets need to have assigned tiering tag
		When a source asset resides in <src_tier>
		And a destination asset resides in <dst_tier>
		Then communication between source and destination is considered <decision2>

		Examples: Tier Jumping Decision Matrix
		| src_tier	| dst_tier	| decision2	|
		| 0		| 3		| tier jumping	|
		| 0		| 2		| no tier-jump	|
		| 1		| 2		| no tier-jump	|
		| 1		| 3		| tier-jumping	|
		| 2		| 3		| no tier-jump	|
		
