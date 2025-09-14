/**
 * La clase AccountLedger gestiona un registro de transacciones para una cuenta bancaria.
 * Hereda de LedgerBase para la funcionalidad básica de la lista enlazada.
 * Añade métodos para calcular saldos y filtrar transacciones.
 */
public class AccountLedger extends LedgerBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el saldo inicial con el que comenzó esta cuenta.
     * Es el punto de partida para calcular el saldo actual.
     */
    private double initialBalance = 0.0;

    /**
     * Almacena la suma de todas las comisiones aplicadas en TODAS las cuentas.
     * Es 'static' para ser un contador global compartido.
     */
    private static double totalFeesApplied = 0.0;


    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Calcula y devuelve el saldo actual de la cuenta.
     * El cálculo es: saldo inicial + la suma de todas las transacciones.
     *
     * @return El saldo actual como un double.
     */
    public double getCurrentBalance() {
        // Usamos una variable local para no modificar el 'initialBalance' original.
        double currentBalance = this.initialBalance;
        Node current = first;

        while (current != null) {
            // Sumamos el 'amount' (puede ser positivo o negativo) al saldo.
            currentBalance += current.value.amount;
            current = current.next;
        }
        return currentBalance;
    }

    /**
     * Devuelve un array con todas las transacciones que son depósitos (amount > 0).
     *
     * @return Un array de objetos Transaction.
     */
    public Transaction[] getDeposits() {
        // Primer recorrido: Contar cuántos depósitos hay.
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.amount > 0) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear el array y rellenarlo.
        Transaction[] deposits = new Transaction[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.amount > 0) {
                deposits[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return deposits;
    }

    /**
     * Encuentra y devuelve la transacción que representa el mayor retiro
     * (el 'amount' negativo con el valor absoluto más alto).
     *
     * @return La transacción del mayor retiro, o null si no hubo retiros.
     */
    public Transaction getLargestWithdrawal() {
        Transaction largestWithdrawal = null;
        double lowestAmount = 0.0; // El récord a batir.
        Node current = first;

        while (current != null) {
            Transaction tx = current.value;
            // Si es un retiro Y su 'amount' es más bajo que nuestro récord actual...
            if (tx.amount < 0 && tx.amount < lowestAmount) {
                // ...tenemos un nuevo "campeón".
                lowestAmount = tx.amount;
                largestWithdrawal = tx;
            }
            current = current.next;
        }
        return largestWithdrawal;
    }

    /**
     * Aplica una comisión a la cuenta. Esto implica añadir una nueva transacción
     * de retiro y actualizar el contador global de comisiones.
     *
     * @param feeAmount   El valor de la comisión (se registrará como negativo).
     * @param description La descripción de la comisión.
     */
    public void applyFee(double feeAmount, String description) {
        // Creamos una nueva transacción con el importe en negativo.
        Transaction feeTransaction = new Transaction(description, -feeAmount);
        // La añadimos a la lista de movimientos de la cuenta.
        addTransaction(feeTransaction);
        // Actualizamos el contador global de comisiones.
        AccountLedger.totalFeesApplied += feeAmount;
    }
}
