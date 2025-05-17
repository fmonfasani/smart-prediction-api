// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MLContract {
    bool public lastPrediction;

    function actualizarEstado(bool _prediccion) public {
        lastPrediction = _prediccion;
    }

    function actuar() public view returns (string memory) {
        if (lastPrediction) {
            return "Acción: Aprobar";
        } else {
            return "Acción: Rechazar";
        }
    }
}
