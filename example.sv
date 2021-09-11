module !TODO! (
	input logic clk;
	input logic n_rst;

	!TODO!

);
	typedef enum logic [1:0] {A, B, C, D} state_t;

	state_t state;
	state_t next_state;

	always_ff @( posedge clk, negedge n_rst ) begin
		if (n_rst == '0) begin
			state <= A;
		end else begin
			state <= next_state;
		end
	end

	// next state logic
	always_comb begin
		next_state = state;
		case (state)
			A: begin
				if (in == 4'b2) begin
					next_state = B;
				end else if (in == 10'b4) begin
					next_state = C;
				end else begin
					next_state = A;
				end
			B: begin
				if (in == 3) begin
					next_state = C;
				end else if (in == 10'b4) begin
					next_state = D;
				end
			C: begin
				if (in == 5) begin
					next_state = D;
				end
			end
			D: begin
				next_state = D;
			end
		endcase
	end

	// output logic
	always_comb begin
	!TODO!
	end

endmodule
