const SEPARATOR = String.fromCharCode(30); // see https://en.wikipedia.org/wiki/Delimiter#ASCII_delimited_text

const encodePayload = (packets, callback) => {
  const length = packets.length;
  const encodedPackets = new Array(length);
  let count = 0;

  packets.forEach((packet, i) => {
    // Implement your encoding logic here if needed
    encodedPackets[i] = packet; // Example: Just store the packet as-is
    if (++count === length) {
      callback(encodedPackets.join(SEPARATOR));
    }
  });
};

const decodePayload = (encodedPayload, binaryType) => {
  const encodedPackets = encodedPayload.split(SEPARATOR);
  const packets = [];
  for (let i = 0; i < encodedPackets.length; i++) {
    // Implement your decoding logic here if needed
    packets.push(encodedPackets[i]); // Example: Just push the encoded packet as-is
  }
  return packets;
};

module.exports = {
  protocol: 4,
  encodePayload,
  decodePayload
};
