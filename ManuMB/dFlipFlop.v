module dffDesign(input clk, din, rst,
                 output reg q, qbar);
    always @(posedge clk) begin
        if (rst) begin
            q <= 0;
            qbar <= ~q;
        end
        else begin
        q <= din;
        qbar <= ~din;
        end
    end
endmodule